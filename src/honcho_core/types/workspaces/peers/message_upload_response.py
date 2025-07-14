# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..sessions.message import Message

__all__ = ["MessageUploadResponse"]

MessageUploadResponse: TypeAlias = List[Message]
