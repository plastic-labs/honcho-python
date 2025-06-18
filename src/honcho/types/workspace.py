# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Workspace"]


class Workspace(BaseModel):
    id: str

    created_at: datetime

    configuration: Optional[Dict[str, object]] = None

    metadata: Optional[Dict[str, object]] = None
