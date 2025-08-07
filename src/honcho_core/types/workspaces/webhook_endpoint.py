# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["WebhookEndpoint"]


class WebhookEndpoint(BaseModel):
    id: str

    created_at: datetime

    url: str

    workspace_id: Optional[str] = None
