import os
from typing import List, Optional

import dspy
from dspy import Example
from chain import StateExtractor, format_chat_history
from dotenv import load_dotenv
from dspy.teleprompt import BootstrapFewShot
from response_metric import metric

from honcho import Honcho
from honcho.types.apps.users.sessions import Message

load_dotenv()

# Configure DSPy
dspy_gpt4 = dspy.OpenAI(model="gpt-4", max_tokens=1000)
dspy.settings.configure(lm=dspy_gpt4)


# DSPy Signatures
class Thought(dspy.Signature):
    """Generate a thought about the user's needs"""

    user_input = dspy.InputField()
    thought = dspy.OutputField(desc="a prediction about the user's mental state")


class Response(dspy.Signature):
    """Generate a response for the user based on the thought provided"""

    user_input = dspy.InputField()
    thought = dspy.InputField()
    response = dspy.OutputField(desc="keep the conversation going, be engaging")


# DSPy Module
class ChatWithThought(dspy.Module):
    generate_thought = dspy.Predict(Thought)
    generate_response = dspy.Predict(Response)

    def forward(
        self,
        chat_input: str,
        honcho: Honcho,
        payload: dict,
        # user_message: Optional[Message] = None,
        # session: Optional[Session] = None,
        response: Optional[str] = None,
        assessment_dimension: Optional[str] = None,
    ):
        # call the thought predictor
        thought = self.generate_thought(user_input=chat_input)

        if payload["session"] and payload["user_message"]:
            # session.create_metamessage(user_message, metamessage_type="thought", content=thought.thought)
            honcho.apps.users.sessions.metamessages.create(
                session_id=payload["session"].id,
                app_id=payload["app"].id,
                user_id=payload["user"].id,
                message_id=payload["message"].id,
                content=thought.thought,
                metamessage_type="thought",
            )

        # call the response predictor
        response = self.generate_response(user_input=chat_input, thought=thought.thought)

        return response  # this is a prediction object


async def chat(
    honcho: Honcho,
    payload: dict,
    chat_history: List[Message],
    input: str,
    optimization_threshold=3,
):
    user_state_storage = dict(payload["user"].metadata)
    # first we need to see if the user has any existing states
    existing_states = list(user_state_storage.keys())

    # then we need to take the user input and determine the user's state/dimension/persona
    is_state_new, user_state = await StateExtractor.generate_state(
        existing_states=existing_states, chat_history=chat_history, input=input
    )
    print(f"USER STATE: {user_state}")
    print(f"IS STATE NEW: {is_state_new}")

    # add metamessage to message to keep track of what label got assigned to what message
    if payload["session"] and payload["message"]:
        honcho.apps.users.sessions.metamessages.create(
            session_id=payload["session"].id,
            app_id=payload["app"].id,
            user_id=payload["user"].id,
            message_id=payload["message"].id,
            content=str(user_state),
            metamessage_type="user_state",
        )

    user_chat_module = ChatWithThought()

    # Save the user_state if it's new
    if is_state_new:
        user_state_storage[user_state] = {"chat_module": {}, "examples": []}

    user_state_data = user_state_storage[user_state]

    # Optimize the state's chat module if we've reached the optimization threshold
    examples = user_state_data["examples"]
    print(f"Num examples: {len(examples)}")
    honcho.apps.users.update(app_id=payload["app"].id, user_id=payload["user"].id, metadata=user_state_storage)

    if len(examples) >= optimization_threshold:
        # convert example from dicts to dspy Example objects
        optimizer_examples = []
        for example in examples:
            optimizer_example = Example(**example).with_inputs("chat_input", "response", "assessment_dimension")
            optimizer_examples.append(optimizer_example)

        # Optimize chat module
        optimizer = BootstrapFewShot(metric=metric, max_rounds=5)

        compiled_chat_module = optimizer.compile(user_chat_module, trainset=optimizer_examples)
        print(f"COMPILED_CHAT_MODULE: {compiled_chat_module}")

        user_state_storage[user_state]["chat_module"] = compiled_chat_module.dump_state()
        print(f"DUMPED_STATE: {compiled_chat_module.dump_state()}")
        user_chat_module = compiled_chat_module

        # Update User in Honcho
        honcho.apps.users.update(app_id=payload["app"].id, user_id=payload["user"].id, metadata=user_state_storage)

    # use that pipeline to generate a response
    chat_input = format_chat_history(chat_history, user_input=input)
    # response = user_chat_module(user_message=user_message, session=session, chat_input=chat_input)
    response = user_chat_module(honcho=honcho, payload=payload, chat_input=chat_input)
    # remove ai prefix
    response = response.response.replace("ai:", "").strip()

    print("========== CHAT HISTORY ==========")
    dspy_gpt4.inspect_history(n=2)
    print("======= END CHAT HISTORY =========")

    return response
