# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Metamessage"]


class Metamessage(BaseModel):
    id: str

    content: str

    created_at: datetime

    message_id: Optional[str] = None

    metadata: Dict[str, object]

    metamessage_type: str

    session_id: Optional[str] = None

    user_id: str
