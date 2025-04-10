# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    app_id: Optional[str]
    """ID of the app to scope the key to"""

    collection_id: Optional[str]
    """ID of the collection to scope the key to"""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    session_id: Optional[str]
    """ID of the session to scope the key to"""

    user_id: Optional[str]
    """ID of the user to scope the key to"""
