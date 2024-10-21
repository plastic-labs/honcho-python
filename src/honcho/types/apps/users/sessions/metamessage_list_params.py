# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MetamessageListParams"]


class MetamessageListParams(TypedDict, total=False):
    app_id: Required[str]

    user_id: Required[str]

    page: int
    """Page number"""

    reverse: Optional[bool]

    size: int
    """Page size"""

    filter: Optional[Dict[str, object]]

    message_id: Optional[str]

    metamessage_type: Optional[str]
