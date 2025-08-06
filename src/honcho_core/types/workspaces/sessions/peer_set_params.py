# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .session_peer_config_param import SessionPeerConfigParam

__all__ = ["PeerSetParams"]


class PeerSetParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    body: Required[Dict[str, SessionPeerConfigParam]]
    """List of peer IDs to set for the session"""
