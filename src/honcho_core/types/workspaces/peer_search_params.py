# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerSearchParams"]


class PeerSearchParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    query: Required[str]
    """Search query"""

    page: int
    """Page number"""

    size: int
    """Page size"""

    semantic: Optional[bool]
    """Whether to explicitly use semantic search to filter the results"""
