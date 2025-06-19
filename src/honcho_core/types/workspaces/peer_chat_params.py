# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PeerChatParams"]


class PeerChatParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    queries: Required[Union[str, List[str]]]

    session_id: Optional[str]
    """ID of the session to scope the representation to"""

    stream: bool

    target: Optional[str]
    """Optional peer to get the representation for, from the perspective of this peer"""
