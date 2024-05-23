"""
Utilities to integrate Honcho with Langchain projects
"""

import functools
import importlib
from typing import List

# from honcho import Session, AsyncSession
from honcho.types.apps.users.sessions import Message


def _requires_langchain(func):
    """A utility to check if langchain is installed before running a function"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Check if langchain is installed before running a function"""

        if importlib.util.find_spec("langchain_core") is None:  # type: ignore
            raise ImportError("Langchain core must be installed to use this feature")
            # raise RuntimeError("langchain is not installed")
        return func(*args, **kwargs)

    return wrapper


@_requires_langchain
def messages_to_langchain(messages: List[Message]):
    """Converts Honcho messages to Langchain messages

    Args:
        messages (List[Message]): The list of messages to convert

    Returns:
        List: The list of converted LangChain messages

    """
    from langchain_core.messages import AIMessage, HumanMessage  # type: ignore

    new_messages = []
    for message in messages:
        if message.is_user:
            new_messages.append(HumanMessage(content=message.content))
        else:
            new_messages.append(AIMessage(content=message.content))
    return new_messages


@_requires_langchain
def langchain_to_messages(messages) -> List[Message]:
    """Converts Langchain messages to Honcho messages and adds to appropriate session

    Args:
        messages: The LangChain messages to convert
        session: The session to add the messages to

    Returns:
        List[Message]: The list of converted messages

    """
    from langchain_core.messages import HumanMessage  # type: ignore

    messages: List[Message] = []
    for message in messages:
        if isinstance(message, HumanMessage):
            new_message = Message(is_user=True, content=message.content, metadata=message.metadata)
            messages.append(new_message)
        else:
            new_message = Message(is_user=False, content=message.content, metadata=message.metadata)
            messages.append(new_message)
    return messages
