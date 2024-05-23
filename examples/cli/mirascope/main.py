import asyncio
from typing import List

from dotenv import load_dotenv
from mirascope.openai import OpenAICall, OpenAICallParams

from honcho import Honcho

load_dotenv()
honcho = Honcho(environment="demo")  # initialize the honcho client
app = honcho.apps.get_or_create("Mirascope Test")  # Get your app instance
user = honcho.apps.users.get_or_create(app_id=app.id, name="test_user")  # Get your user
session = honcho.apps.users.sessions.create(app_id=app.id, user_id=user.id, location_id="cli")  # Make a new session


# Set up your OpenAI Call
class Conversation(OpenAICall):
    prompt_template = """
    SYSTEM: 
    You are a helpful assistant that provides incredibly short and efficient
    responses.

    MESSAGES: {history}
    
    USER: 
    {user_input}
    """
    user_input: str
    session_id: str
    app_id: str
    user_id: str

    @property
    def history(self) -> List[dict]:
        """Get the conversation history from Honcho"""
        history_list = []
        iter = honcho.apps.users.sessions.messages.list(
            session_id=self.session_id, app_id=self.app_id, user_id=self.user_id
        )
        for message in iter:
            if message.is_user:
                history_list.append({"role": "user", "content": message.content})
            else:
                history_list.append({"role": "assistant", "content": message.content})
        return history_list

    # context: str
    call_params = OpenAICallParams(model="gpt-4o-2024-05-13", temperature=0.4)


conversation = Conversation(user_input="", app_id=app.id, user_id=user.id, session_id=session.id)


async def chat():
    while True:
        conversation.user_input = input(">>> ")
        if conversation.user_input == "exit":
            honcho.apps.users.sessions.delete(session_id=session.id, app_id=app.id, user_id=user.id)
            break
        response = ""
        cstream = conversation.stream_async()
        print("\033[96mAI:\033[0m")
        async for chunk in cstream:
            print(f"\033[96m{chunk.content}\033[0m", end="", flush=True)
            response += chunk.content
        print("\n")

        # Save User and AI messages to Honcho
        honcho.apps.users.sessions.messages.create(
            session_id=session.id, app_id=app.id, user_id=user.id, content=conversation.user_input, is_user=True
        )
        honcho.apps.users.sessions.messages.create(
            session_id=session.id, app_id=app.id, user_id=user.id, content=response, is_user=False
        )


if __name__ == "__main__":
    asyncio.run(chat())
