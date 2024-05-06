# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .message import Message
from ....._models import BaseModel

__all__ = ["PageMessage"]


class PageMessage(BaseModel):
    items: List[Message]

    page: int

    size: int

    total: int

    pages: Optional[int] = None
