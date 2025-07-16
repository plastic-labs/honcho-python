# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .message_create_param import MessageCreateParam

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    workspace_id: Required[str]

    messages: Required[Iterable[MessageCreateParam]]
