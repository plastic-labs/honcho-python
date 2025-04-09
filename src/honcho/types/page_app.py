# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .app import App
from .._models import BaseModel

__all__ = ["PageApp"]


class PageApp(BaseModel):
    items: List[App]

    page: int

    size: int

    total: int

    pages: Optional[int] = None
