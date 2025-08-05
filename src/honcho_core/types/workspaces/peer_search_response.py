# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .sessions.message import Message

__all__ = ["PeerSearchResponse"]

PeerSearchResponse: TypeAlias = List[Message]
