# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerAddParams", "Body"]


class PeerAddParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    body: Required[Dict[str, Body]]
    """List of peer IDs to add to the session"""


class Body(TypedDict, total=False):
    observe_me: Optional[bool]
    """
    Whether other peers in this session should try to form a session-level
    theory-of-mind representation of this peer
    """

    observe_others: bool
    """
    Whether this peer should form a session-level theory-of-mind representation of
    other peers in the session
    """
