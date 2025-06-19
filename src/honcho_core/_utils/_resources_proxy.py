from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `honcho_core.resources` module.

    This is used so that we can lazily import `honcho_core.resources` only when
    needed *and* so that users can just import `honcho_core` and reference `honcho_core.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("honcho_core.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
