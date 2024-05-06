# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.apps.users.collection import Collection

__all__ = ["NameResource", "AsyncNameResource"]


class NameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NameResourceWithRawResponse:
        return NameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NameResourceWithStreamingResponse:
        return NameResourceWithStreamingResponse(self)

    def retrieve(
        self,
        name: str,
        *,
        app_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Get Collection By Name

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
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/apps/{app_id}/users/{user_id}/collections/name/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )


class AsyncNameResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNameResourceWithRawResponse:
        return AsyncNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNameResourceWithStreamingResponse:
        return AsyncNameResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        name: str,
        *,
        app_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Get Collection By Name

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
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/apps/{app_id}/users/{user_id}/collections/name/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )


class NameResourceWithRawResponse:
    def __init__(self, name: NameResource) -> None:
        self._name = name

        self.retrieve = to_raw_response_wrapper(
            name.retrieve,
        )


class AsyncNameResourceWithRawResponse:
    def __init__(self, name: AsyncNameResource) -> None:
        self._name = name

        self.retrieve = async_to_raw_response_wrapper(
            name.retrieve,
        )


class NameResourceWithStreamingResponse:
    def __init__(self, name: NameResource) -> None:
        self._name = name

        self.retrieve = to_streamed_response_wrapper(
            name.retrieve,
        )


class AsyncNameResourceWithStreamingResponse:
    def __init__(self, name: AsyncNameResource) -> None:
        self._name = name

        self.retrieve = async_to_streamed_response_wrapper(
            name.retrieve,
        )