# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["SessionChatParams"]


class SessionChatParams(TypedDict, total=False):
    app_id: Required[str]

    user_id: Required[str]

    queries: Required[Union[str, List[str]]]
