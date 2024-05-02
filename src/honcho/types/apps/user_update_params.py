# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserUpdateParams", "Metadata"]


class UserUpdateParams(TypedDict, total=False):
    app_id: Required[str]

    metadata: Optional[Metadata]

    name: Optional[str]


class Metadata(TypedDict, total=False):
    pass
