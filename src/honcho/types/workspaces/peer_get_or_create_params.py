# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["PeerGetOrCreateParams"]


class PeerGetOrCreateParams(TypedDict, total=False):
    id: Required[str]

    feature_flags: Dict[str, object]

    metadata: Dict[str, object]
