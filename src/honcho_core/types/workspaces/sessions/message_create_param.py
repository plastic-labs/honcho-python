# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MessageCreateParam"]


class MessageCreateParam(TypedDict, total=False):
    content: Required[str]

    peer_id: Required[str]

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    metadata: Optional[Dict[str, object]]
