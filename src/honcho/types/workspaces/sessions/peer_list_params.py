# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PeerListParams"]


class PeerListParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    page: int
    """Page number"""

    size: int
    """Page size"""
