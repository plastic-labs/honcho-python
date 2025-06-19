# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    peer_id: Optional[str]
    """ID of the peer to scope the key to"""

    session_id: Optional[str]
    """ID of the session to scope the key to"""

    workspace_id: Optional[str]
    """ID of the workspace to scope the key to"""
