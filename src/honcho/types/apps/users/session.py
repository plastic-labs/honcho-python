# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    id: str

    created_at: datetime

    is_active: bool

    location_id: str

    metadata: Dict[str, object]

    user_id: str
