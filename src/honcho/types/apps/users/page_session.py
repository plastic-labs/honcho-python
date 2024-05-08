# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .session import Session
from ...._models import BaseModel

__all__ = ["PageSession"]


class PageSession(BaseModel):
    items: List[Session]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
