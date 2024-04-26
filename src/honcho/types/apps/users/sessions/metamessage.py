# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ....._models import BaseModel

__all__ = ["Metamessage"]


class Metamessage(BaseModel):
    id: str

    content: str

    created_at: datetime

    message_id: str

    metadata: object

    metamessage_type: str
