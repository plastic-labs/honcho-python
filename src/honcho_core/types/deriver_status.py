# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["DeriverStatus"]


class DeriverStatus(BaseModel):
    completed_work_units: int
    """Completed work units"""

    in_progress_work_units: int
    """Work units currently being processed"""

    pending_work_units: int
    """Work units waiting to be processed"""

    total_work_units: int
    """Total work units"""

    peer_id: Optional[str] = None
    """ID of the peer (optional when filtering by session only)"""

    session_id: Optional[str] = None
    """Session ID if filtered by session"""

    sessions: Optional[Dict[str, "DeriverStatus"]] = None
    """Per-session status when not filtered by session"""


if PYDANTIC_V2:
    DeriverStatus.model_rebuild()
else:
    DeriverStatus.update_forward_refs()  # type: ignore
