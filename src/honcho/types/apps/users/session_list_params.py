# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    app_id: Required[str]
    """ID of the app"""

    page: int
    """Page number"""

    reverse: Optional[bool]
    """Whether to reverse the order of results"""

    size: int
    """Page size"""

    filter: Optional[Dict[str, object]]

    is_active: bool
