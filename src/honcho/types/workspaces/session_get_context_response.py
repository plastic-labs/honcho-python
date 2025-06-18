# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .sessions.message import Message

__all__ = ["SessionGetContextResponse"]


class SessionGetContextResponse(BaseModel):
    id: str

    messages: List[Message]

    summary: str
