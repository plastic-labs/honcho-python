# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MetamessageUpdateParams", "Metadata"]


class MetamessageUpdateParams(TypedDict, total=False):
    app_id: Required[str]

    user_id: Required[str]

    session_id: Required[str]

    message_id: Required[str]

    metadata: Optional[Metadata]

    metamessage_type: Optional[str]


class Metadata(TypedDict, total=False):
    pass