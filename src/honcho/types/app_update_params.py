# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AppUpdateParams", "Metadata"]


class AppUpdateParams(TypedDict, total=False):
    metadata: Optional[Metadata]

    name: Optional[str]


class Metadata(TypedDict, total=False):
    pass
