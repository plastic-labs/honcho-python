# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MessageUpdateParams"]


class MessageUpdateParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    session_id: Required[str]
    """ID of the session"""

    metadata: Optional[Dict[str, object]]
