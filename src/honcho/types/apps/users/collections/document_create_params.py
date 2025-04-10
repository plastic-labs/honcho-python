# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    app_id: Required[str]
    """ID of the app"""

    user_id: Required[str]
    """ID of the user"""

    content: Required[str]

    metadata: Dict[str, object]
