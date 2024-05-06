# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentUpdateParams"]


class DocumentUpdateParams(TypedDict, total=False):
    app_id: Required[str]

    user_id: Required[str]

    collection_id: Required[str]

    content: Optional[str]

    metadata: Optional[object]
