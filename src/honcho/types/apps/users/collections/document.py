# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["Document"]


class Document(BaseModel):
    id: str

    app_id: str

    collection_id: str

    content: str

    created_at: datetime

    user_id: str

    metadata: Optional[Dict[str, object]] = None
