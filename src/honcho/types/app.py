# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["App"]


class App(BaseModel):
    id: str

    created_at: datetime

    metadata: object

    name: str
