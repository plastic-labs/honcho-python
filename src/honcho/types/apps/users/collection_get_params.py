# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CollectionGetParams"]


class CollectionGetParams(TypedDict, total=False):
    app_id: Required[str]
    """ID of the app"""

    collection_id: Optional[str]
    """Collection ID to retrieve. If not provided, uses JWT token"""
