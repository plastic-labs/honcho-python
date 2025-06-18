# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["PeerSetParams", "Body"]


class PeerSetParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    body: Required[Dict[str, Body]]
    """List of peer IDs to set for the session"""


class Body(TypedDict, total=False):
    observe_me: bool
    """
    Whether other peers in this session should try to form a session-level
    theory-of-mind representation of this peer
    """

    observe_others: bool
    """
    Whether this peer should form a session-level theory-of-mind representation of
    other peers in the session
    """
