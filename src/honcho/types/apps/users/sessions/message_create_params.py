# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageCreateParams", "Metadata"]


class MessageCreateParams(TypedDict, total=False):
    app_id: Required[str]

    user_id: Required[str]

    content: Required[str]

    is_user: Required[bool]

    metadata: Optional[Metadata]


class Metadata(TypedDict, total=False):
    pass
