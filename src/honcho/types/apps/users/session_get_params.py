# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionGetParams"]


class SessionGetParams(TypedDict, total=False):
    app_id: Required[str]
    """ID of the app"""

    session_id: Optional[str]
    """Session ID to retrieve. If not provided, uses JWT token"""
