# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["MessageUpdateParams"]


class MessageUpdateParams(TypedDict, total=False):
    app_id: Required[str]

    user_id: Required[str]

    session_id: Required[str]

    metadata: Required[Dict[str, object]]
