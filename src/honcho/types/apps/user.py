# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from ..._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str

    app_id: str

    created_at: datetime

    metadata: Dict[str, object]

    name: str
