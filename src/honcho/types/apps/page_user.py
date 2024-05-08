# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .user import User
from ..._models import BaseModel

__all__ = ["PageUser"]


class PageUser(BaseModel):
    items: List[User]

    page: int

    size: int

    total: int

    pages: Optional[int] = None
