# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .peer import Peer
from ..._models import BaseModel

__all__ = ["PagePeer"]


class PagePeer(BaseModel):
    items: List[Peer]

    page: int

    size: int

    pages: Optional[int] = None

    total: Optional[int] = None
