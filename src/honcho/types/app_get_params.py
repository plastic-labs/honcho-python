# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AppGetParams"]


class AppGetParams(TypedDict, total=False):
    app_id: Optional[str]
    """App ID to retrieve. If not provided, uses JWT token"""
