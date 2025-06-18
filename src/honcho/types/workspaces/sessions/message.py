# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Message"]


class Message(BaseModel):
    id: str

    content: str

    created_at: datetime

    peer_name: str

    session_name: Optional[str] = None

    token_count: int

    workspace_name: str

    metadata: Optional[Dict[str, object]] = None
