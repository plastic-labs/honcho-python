# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserGetParams"]


class UserGetParams(TypedDict, total=False):
    user_id: Optional[str]
    """User ID to retrieve. If not provided, users JWT token"""
