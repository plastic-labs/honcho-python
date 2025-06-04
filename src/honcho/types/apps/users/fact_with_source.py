from __future__ import annotations

from typing import Optional

from ...._models import BaseModel

__all__ = ["FactWithSource"]


class FactWithSource(BaseModel):
    """A retrieved fact along with a snippet of its source message."""

    fact: str
    message_id: Optional[str] = None
    message_content: Optional[str] = None 