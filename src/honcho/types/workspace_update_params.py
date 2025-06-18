# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["WorkspaceUpdateParams"]


class WorkspaceUpdateParams(TypedDict, total=False):
    configuration: Optional[Dict[str, object]]

    metadata: Optional[Dict[str, object]]
