# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MetamessageCreateParams"]


class MetamessageCreateParams(TypedDict, total=False):
    app_id: Required[str]
    """ID of the app"""

    content: Required[str]

    metamessage_type: Required[str]

    message_id: Optional[str]

    metadata: Dict[str, object]

    session_id: Optional[str]
