# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .sessions.session_peer_config_param import SessionPeerConfigParam

__all__ = ["SessionGetOrCreateParams"]


class SessionGetOrCreateParams(TypedDict, total=False):
    id: Required[str]

    configuration: Optional[Dict[str, object]]

    metadata: Optional[Dict[str, object]]

    peers: Optional[Dict[str, SessionPeerConfigParam]]
