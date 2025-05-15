# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Metamessage"]


class Metamessage(BaseModel):
    id: str

    app_id: str

    content: str

    created_at: datetime

    label: str

    message_id: Optional[str] = None

    metamessage_type: str

    session_id: Optional[str] = None

    user_id: str

    metadata: Optional[Dict[str, object]] = None
