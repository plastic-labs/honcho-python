# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ....._models import BaseModel

__all__ = ["Message"]


class Message(BaseModel):
    id: str

    content: str

    created_at: datetime

    is_user: bool

    metadata: object

    session_id: str
