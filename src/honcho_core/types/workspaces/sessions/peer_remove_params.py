# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["PeerRemoveParams"]


class PeerRemoveParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    body: Required[List[str]]
    """List of peer IDs to remove from the session"""
