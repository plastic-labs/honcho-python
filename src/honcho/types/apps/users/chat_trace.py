from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from .fact_with_source import FactWithSource

__all__ = ["ChatTrace"]


class ChatTrace(BaseModel):
    """Debug payload returned when include_trace=True."""

    queries: List[str]
    facts: List[FactWithSource]
    tom_inference: str
    user_representation: Optional[str] = None
    latency_ms: Optional[float] = None 