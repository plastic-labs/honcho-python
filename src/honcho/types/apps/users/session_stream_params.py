# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionStreamParams"]


class SessionStreamParams(TypedDict, total=False):
    app_id: Required[str]

    user_id: Required[str]

    query: Required[str]
