# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["QueryListParams"]


class QueryListParams(TypedDict, total=False):
    app_id: Required[str]

    user_id: Required[str]

    query: Required[str]

    filter: Optional[str]

    top_k: int
