# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["Collection", "Metadata"]


class Metadata(BaseModel):
    pass


class Collection(BaseModel):
    id: str

    created_at: datetime

    metadata: Metadata

    name: str

    user_id: str
