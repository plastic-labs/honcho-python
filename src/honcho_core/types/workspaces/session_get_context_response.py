# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .sessions.message import Message

__all__ = ["SessionGetContextResponse", "Summary"]


class Summary(BaseModel):
    content: str
    """The summary text"""

    created_at: str
    """The timestamp of when the summary was created (ISO format)"""

    message_id: int
    """The ID of the message that this summary covers up to"""

    summary_type: str
    """The type of summary (short or long)"""

    token_count: int
    """The number of tokens in the summary text"""


class SessionGetContextResponse(BaseModel):
    id: str

    messages: List[Message]

    summary: Optional[Summary] = None
    """The summary if available"""
