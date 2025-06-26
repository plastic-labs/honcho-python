# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionGetOrCreateParams", "Peers"]


class SessionGetOrCreateParams(TypedDict, total=False):
    id: Required[str]

    configuration: Optional[Dict[str, object]]

    metadata: Optional[Dict[str, object]]

    peers: Optional[Dict[str, Peers]]


class Peers(TypedDict, total=False):
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
