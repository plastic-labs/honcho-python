# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkspaceSearchParams"]


class WorkspaceSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query"""

    limit: int
    """Number of results to return"""
