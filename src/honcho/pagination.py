# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPage", "AsyncPage"]

_T = TypeVar("_T")


class SyncPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    total: Union[int, str, None] = None
    items: List[_T]
    page: Union[int, object, None] = None
    size: Union[int, object, None] = None
    pages: Union[int, object, None] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        last_page = cast("int | None", self._options.params.get("page"))
        if last_page is not None and current_page <= last_page:
            # The API didn't return a new page in the last request
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    total: Union[int, str, None] = None
    items: List[_T]
    page: Union[int, object, None] = None
    size: Union[int, object, None] = None
    pages: Union[int, object, None] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        last_page = cast("int | None", self._options.params.get("page"))
        if last_page is not None and current_page <= last_page:
            # The API didn't return a new page in the last request
            return None

        return PageInfo(params={"page": current_page + 1})
