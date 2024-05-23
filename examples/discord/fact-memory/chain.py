import os
from typing import List

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    load_prompt,
)
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import NumberedListOutputParser

from honcho import Honcho

load_dotenv()

SYSTEM_DERIVE_FACTS = load_prompt(os.path.join(os.path.dirname(__file__), "prompts/core/derive_facts.yaml"))
SYSTEM_INTROSPECTION = load_prompt(os.path.join(os.path.dirname(__file__), "prompts/core/introspection.yaml"))
SYSTEM_RESPONSE = load_prompt(os.path.join(os.path.dirname(__file__), "prompts/core/response.yaml"))
SYSTEM_CHECK_DUPS = load_prompt(os.path.join(os.path.dirname(__file__), "prompts/utils/check_dup_facts.yaml"))


class LMChain:
    "Wrapper class for encapsulating the multiple different chains used"

    output_parser = NumberedListOutputParser()
    llm: ChatOpenAI = ChatOpenAI(model_name="gpt-3.5-turbo")  # type: ignore
    system_derive_facts: SystemMessagePromptTemplate = SystemMessagePromptTemplate(prompt=SYSTEM_DERIVE_FACTS)  # type: ignore
    system_introspection: SystemMessagePromptTemplate = SystemMessagePromptTemplate(prompt=SYSTEM_INTROSPECTION)  # type: ignore
    system_response: SystemMessagePromptTemplate = SystemMessagePromptTemplate(prompt=SYSTEM_RESPONSE)  # type: ignore
    system_check_dups: SystemMessagePromptTemplate = SystemMessagePromptTemplate(prompt=SYSTEM_CHECK_DUPS)  # type: ignore

    honcho = Honcho(environment="demo")

    def __init__(self) -> None:
        pass

    @classmethod
    async def derive_facts(cls, chat_history: List, input: str):
        """Derive facts from the user input"""

        # format prompt
        fact_derivation = ChatPromptTemplate.from_messages([cls.system_derive_facts])

        # LCEL
        chain = fact_derivation | cls.llm

        # inference
        response = await chain.ainvoke(
            {
                "chat_history": [
                    ("user: " + message.content if isinstance(message, HumanMessage) else "ai: " + message.content)  # type: ignore
                    for message in chat_history
                ],
                "user_input": input,
            }
        )

        # parse output
        facts = cls.output_parser.parse(response.content)  # type: ignore

        print(f"DERIVED FACTS: {facts}")

        return facts

    @classmethod
    async def check_dups(
        cls,
        payload: dict,
        facts: List,
    ):
        """Check that we're not storing duplicate facts"""

        # format prompt
        check_duplication = ChatPromptTemplate.from_messages([cls.system_check_dups])

        query = " ".join(facts)
        result = cls.honcho.apps.users.collections.query(
            app_id=payload["app"], user_id=payload["user"], collection_id=payload["collection"], query=query, top_k=10
        )
        existing_facts = [document.content for document in result]

        # LCEL
        chain = check_duplication | cls.llm

        # inference
        response = await chain.ainvoke({"existing_facts": existing_facts, "facts": facts})

        # parse output
        new_facts = cls.output_parser.parse(response.content)  # type: ignore

        print(f"FILTERED FACTS: {new_facts}")

        # TODO: write to vector store
        for fact in new_facts:
            cls.honcho.apps.users.collections.documents.create(
                app_id=payload["app"], user_id=payload["user"], collection_id=payload["collection"], content=fact
            )

        # add facts as metamessages
        for fact in new_facts:
            cls.honcho.apps.users.sessions.metamessages.create(
                user_id=payload["user"],
                app_id=payload["app"],
                session_id=payload["session"],
                message_id=payload["message"],
                metamessage_type="fact",
                content=fact,
            )

        return

    @classmethod
    async def introspect(cls, payload: dict, chat_history: List, input: str):
        """Generate questions about the user to use as retrieval over the fact store"""

        # format prompt
        introspection_prompt = ChatPromptTemplate.from_messages([cls.system_introspection])

        # LCEL
        chain = introspection_prompt | cls.llm

        # inference
        response = await chain.ainvoke({"chat_history": chat_history, "user_input": input})

        # parse output
        questions = cls.output_parser.parse(response.content)  # type: ignore

        print(f"INTROSPECTED QUESTIONS: {questions}")

        # write questions as metamessages
        for question in questions:
            cls.honcho.apps.users.sessions.metamessages.create(
                user_id=payload["user"],
                app_id=payload["app"],
                session_id=payload["session"],
                message_id=payload["message"],
                metamessage_type="introspect",
                content=question,
            )

        return questions

    @classmethod
    async def respond(cls, payload: dict, chat_history: List, questions: List, input: str):
        """Take the facts and chat history and generate a personalized response"""

        # format prompt
        response_prompt = ChatPromptTemplate.from_messages(
            [cls.system_response, *chat_history, HumanMessage(content=input)]
        )

        query = " ".join(questions)
        retrieved_facts = cls.honcho.apps.users.collections.query(
            app_id=payload["app"], user_id=payload["user"], collection_id=payload["collection"], query=query, top_k=10
        )

        retrieved_facts_content = [document.content for document in retrieved_facts]

        # LCEL
        chain = response_prompt | cls.llm

        # inference
        response = await chain.ainvoke(
            {
                "facts": retrieved_facts_content,
            }
        )

        return response.content

    @classmethod
    async def chat(
        cls,
        chat_history: List,
        payload: dict,
        input: str,
    ):
        """Chat with the model"""

        facts = await cls.derive_facts(chat_history, input)
        await cls.check_dups(payload, facts) if facts is not None else None

        # introspect
        questions = await cls.introspect(payload, chat_history, input)

        # respond
        response = await cls.respond(payload, chat_history, questions, input)

        return response
