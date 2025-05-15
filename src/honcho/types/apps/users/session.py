# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    id: str

    app_id: str

    created_at: datetime

    is_active: bool

    user_id: str

    metadata: Optional[Dict[str, object]] = None
