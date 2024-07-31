# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    app_id: Required[str]

    filter: Optional[str]

    is_active: Optional[bool]

    page: int
    """Page number"""

    reverse: Optional[bool]

    size: int
    """Page size"""
