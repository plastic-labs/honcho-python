# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionGetContextParams"]


class SessionGetContextParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    summary: bool
    """Whether or not to include a summary _if_ one is available for the session"""

    tokens: Optional[int]
    """Number of tokens to use for the context.

    Includes summary if set to true. If not provided, the context will be exhaustive
    (within 100000 tokens)
    """
