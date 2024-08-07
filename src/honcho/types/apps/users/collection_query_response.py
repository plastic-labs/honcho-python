# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .collections.document import Document

__all__ = ["CollectionQueryResponse"]

CollectionQueryResponse: TypeAlias = List[Document]
