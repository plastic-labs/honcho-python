# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["AppUpdateParams"]


class AppUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, object]]

    name: Optional[str]
