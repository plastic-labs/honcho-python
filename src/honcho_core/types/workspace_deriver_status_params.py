# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["WorkspaceDeriverStatusParams"]


class WorkspaceDeriverStatusParams(TypedDict, total=False):
    include_sender: bool
    """Include work units triggered by this peer"""

    peer_id: Optional[str]
    """Optional peer ID to filter by"""

    session_id: Optional[str]
    """Optional session ID to filter by"""
