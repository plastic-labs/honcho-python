# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .metamessage import Metamessage

__all__ = ["PageMetamessage"]


class PageMetamessage(BaseModel):
    items: List[Metamessage]

    page: int

    size: int

    total: int

    pages: Optional[int] = None
