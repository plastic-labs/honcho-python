# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    app_id: Required[str]

    location_id: Required[str]

    metadata: Optional[Dict[str, object]]
