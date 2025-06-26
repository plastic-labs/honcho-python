# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    page: int
    """Page number"""

    size: int
    """Page size"""

    filter: Optional[Dict[str, object]]
