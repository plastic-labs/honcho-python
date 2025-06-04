# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .chat_trace import ChatTrace

__all__ = ["DialecticResponse"]


class DialecticResponse(BaseModel):
    content: str
    trace: Optional[ChatTrace] = None
