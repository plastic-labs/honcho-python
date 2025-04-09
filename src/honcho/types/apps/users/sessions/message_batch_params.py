# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MessageBatchParams", "Message"]


class MessageBatchParams(TypedDict, total=False):
    app_id: Required[str]
    """ID of the app"""

    user_id: Required[str]
    """ID of the user"""

    messages: Required[Iterable[Message]]


class Message(TypedDict, total=False):
    content: Required[str]

    is_user: Required[bool]

    metadata: Dict[str, object]
