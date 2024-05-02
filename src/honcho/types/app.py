# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["App", "Metadata"]


class Metadata(BaseModel):
    pass


class App(BaseModel):
    id: str

    created_at: datetime

    metadata: Metadata

    name: str
