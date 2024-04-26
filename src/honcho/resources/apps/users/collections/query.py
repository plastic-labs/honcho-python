# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import (
    make_request_options,
)
from .....types.apps.users.collections import query_list_params
from .....types.apps.users.collections.query_list_response import QueryListResponse

__all__ = ["QueryResource", "AsyncQueryResource"]


class QueryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self)

    def list(
        self,
        collection_id: str,
        *,
        app_id: str,
        user_id: str,
        query: str,
        filter: Optional[str] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryListResponse:
        """
        Query Documents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return self._get(
            f"/apps/{app_id}/users/{user_id}/collections/{collection_id}/query",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "filter": filter,
                        "top_k": top_k,
                    },
                    query_list_params.QueryListParams,
                ),
            ),
            cast_to=QueryListResponse,
        )


class AsyncQueryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self)

    async def list(
        self,
        collection_id: str,
        *,
        app_id: str,
        user_id: str,
        query: str,
        filter: Optional[str] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryListResponse:
        """
        Query Documents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not collection_id:
            raise ValueError(f"Expected a non-empty value for `collection_id` but received {collection_id!r}")
        return await self._get(
            f"/apps/{app_id}/users/{user_id}/collections/{collection_id}/query",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "filter": filter,
                        "top_k": top_k,
                    },
                    query_list_params.QueryListParams,
                ),
            ),
            cast_to=QueryListResponse,
        )


class QueryResourceWithRawResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.list = to_raw_response_wrapper(
            query.list,
        )


class AsyncQueryResourceWithRawResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.list = async_to_raw_response_wrapper(
            query.list,
        )


class QueryResourceWithStreamingResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.list = to_streamed_response_wrapper(
            query.list,
        )


class AsyncQueryResourceWithStreamingResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.list = async_to_streamed_response_wrapper(
            query.list,
        )
