# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .collection import Collection

__all__ = ["PageCollection"]


class PageCollection(BaseModel):
    items: List[Collection]

    page: int

    size: int

    total: int

    pages: Optional[int] = None
