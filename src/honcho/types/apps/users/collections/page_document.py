# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .document import Document
from ....._models import BaseModel

__all__ = ["PageDocument"]


class PageDocument(BaseModel):
    items: List[Document]

    page: Optional[int] = None

    size: Optional[int] = None

    total: Optional[int] = None

    pages: Optional[int] = None
