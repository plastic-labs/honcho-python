# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .document import Document
from ....._models import BaseModel

__all__ = ["PageDocument"]


class PageDocument(BaseModel):
    items: List[Document]

    page: int

    size: int

    total: int

    pages: Optional[int] = None
