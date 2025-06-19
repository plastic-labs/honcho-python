# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionSearchParams"]


class SessionSearchParams(TypedDict, total=False):
    workspace_id: Required[str]
    """ID of the workspace"""

    body: Required[str]
    """Search query"""

    page: int
    """Page number"""

    size: int
    """Page size"""
