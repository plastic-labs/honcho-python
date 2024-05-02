# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ....._models import BaseModel

__all__ = ["Document", "Metadata"]


class Metadata(BaseModel):
    pass


class Document(BaseModel):
    id: str

    collection_id: str

    content: str

    created_at: datetime

    metadata: Metadata