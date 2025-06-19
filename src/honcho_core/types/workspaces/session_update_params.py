# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionUpdateParams"]


class SessionUpdateParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    configuration: Optional[Dict[str, object]]

    metadata: Optional[Dict[str, object]]
