# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.apps.users import metamessage_list_params, metamessage_create_params, metamessage_update_params
from ....types.apps.users.metamessage import Metamessage

__all__ = ["MetamessagesResource", "AsyncMetamessagesResource"]


class MetamessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetamessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python#accessing-raw-response-data-eg-headers
        """
        return MetamessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetamessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python#with_streaming_response
        """
        return MetamessagesResourceWithStreamingResponse(self)

    def create(
        self,
        user_id: str,
        *,
        app_id: str,
        content: str,
        metamessage_type: str,
        message_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """Create a new metamessage associated with a user.

        Optionally link to a session
        and message by providing those IDs in the request body.

        Args:
          app_id: ID of the app

          user_id: ID of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            f"/v1/apps/{app_id}/users/{user_id}/metamessages",
            body=maybe_transform(
                {
                    "content": content,
                    "metamessage_type": metamessage_type,
                    "message_id": message_id,
                    "metadata": metadata,
                    "session_id": session_id,
                },
                metamessage_create_params.MetamessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )

    def update(
        self,
        metamessage_id: str,
        *,
        app_id: str,
        user_id: str,
        message_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Update a metamessage's metadata, type, or relationships

        Args:
          app_id: ID of the app

          user_id: ID of the user

          metamessage_id: ID of the metamessage to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not metamessage_id:
            raise ValueError(f"Expected a non-empty value for `metamessage_id` but received {metamessage_id!r}")
        return self._put(
            f"/v1/apps/{app_id}/users/{user_id}/metamessages/{metamessage_id}",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "metadata": metadata,
                    "metamessage_type": metamessage_type,
                    "session_id": session_id,
                },
                metamessage_update_params.MetamessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )

    def list(
        self,
        user_id: str,
        *,
        app_id: str,
        page: int | NotGiven = NOT_GIVEN,
        reverse: Optional[bool] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        filter: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message_id: Optional[str] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Metamessage]:
        """
        Get metamessages with flexible filtering.

        - Filter by user only: No additional parameters needed
        - Filter by session: Provide session_id
        - Filter by message: Provide message_id (and session_id)
        - Filter by type: Provide label
        - Filter by metadata: Provide filter object

        Args:
          app_id: ID of the app

          user_id: ID of the user

          page: Page number

          reverse: Whether to reverse the order of results

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/v1/apps/{app_id}/users/{user_id}/metamessages/list",
            page=SyncPage[Metamessage],
            body=maybe_transform(
                {
                    "filter": filter,
                    "message_id": message_id,
                    "metamessage_type": metamessage_type,
                    "session_id": session_id,
                },
                metamessage_list_params.MetamessageListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "reverse": reverse,
                        "size": size,
                    },
                    metamessage_list_params.MetamessageListParams,
                ),
            ),
            model=Metamessage,
            method="post",
        )

    def get(
        self,
        metamessage_id: str,
        *,
        app_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Get a specific Metamessage by ID

        Args:
          app_id: ID of the app

          user_id: ID of the user

          metamessage_id: ID of the metamessage to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not metamessage_id:
            raise ValueError(f"Expected a non-empty value for `metamessage_id` but received {metamessage_id!r}")
        return self._get(
            f"/v1/apps/{app_id}/users/{user_id}/metamessages/{metamessage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )


class AsyncMetamessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetamessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetamessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetamessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python#with_streaming_response
        """
        return AsyncMetamessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        user_id: str,
        *,
        app_id: str,
        content: str,
        metamessage_type: str,
        message_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """Create a new metamessage associated with a user.

        Optionally link to a session
        and message by providing those IDs in the request body.

        Args:
          app_id: ID of the app

          user_id: ID of the user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            f"/v1/apps/{app_id}/users/{user_id}/metamessages",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "metamessage_type": metamessage_type,
                    "message_id": message_id,
                    "metadata": metadata,
                    "session_id": session_id,
                },
                metamessage_create_params.MetamessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )

    async def update(
        self,
        metamessage_id: str,
        *,
        app_id: str,
        user_id: str,
        message_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Update a metamessage's metadata, type, or relationships

        Args:
          app_id: ID of the app

          user_id: ID of the user

          metamessage_id: ID of the metamessage to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not metamessage_id:
            raise ValueError(f"Expected a non-empty value for `metamessage_id` but received {metamessage_id!r}")
        return await self._put(
            f"/v1/apps/{app_id}/users/{user_id}/metamessages/{metamessage_id}",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "metadata": metadata,
                    "metamessage_type": metamessage_type,
                    "session_id": session_id,
                },
                metamessage_update_params.MetamessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )

    def list(
        self,
        user_id: str,
        *,
        app_id: str,
        page: int | NotGiven = NOT_GIVEN,
        reverse: Optional[bool] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        filter: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        message_id: Optional[str] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Metamessage, AsyncPage[Metamessage]]:
        """
        Get metamessages with flexible filtering.

        - Filter by user only: No additional parameters needed
        - Filter by session: Provide session_id
        - Filter by message: Provide message_id (and session_id)
        - Filter by type: Provide label
        - Filter by metadata: Provide filter object

        Args:
          app_id: ID of the app

          user_id: ID of the user

          page: Page number

          reverse: Whether to reverse the order of results

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get_api_list(
            f"/v1/apps/{app_id}/users/{user_id}/metamessages/list",
            page=AsyncPage[Metamessage],
            body=maybe_transform(
                {
                    "filter": filter,
                    "message_id": message_id,
                    "metamessage_type": metamessage_type,
                    "session_id": session_id,
                },
                metamessage_list_params.MetamessageListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "reverse": reverse,
                        "size": size,
                    },
                    metamessage_list_params.MetamessageListParams,
                ),
            ),
            model=Metamessage,
            method="post",
        )

    async def get(
        self,
        metamessage_id: str,
        *,
        app_id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Get a specific Metamessage by ID

        Args:
          app_id: ID of the app

          user_id: ID of the user

          metamessage_id: ID of the metamessage to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not metamessage_id:
            raise ValueError(f"Expected a non-empty value for `metamessage_id` but received {metamessage_id!r}")
        return await self._get(
            f"/v1/apps/{app_id}/users/{user_id}/metamessages/{metamessage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )


class MetamessagesResourceWithRawResponse:
    def __init__(self, metamessages: MetamessagesResource) -> None:
        self._metamessages = metamessages

        self.create = to_raw_response_wrapper(
            metamessages.create,
        )
        self.update = to_raw_response_wrapper(
            metamessages.update,
        )
        self.list = to_raw_response_wrapper(
            metamessages.list,
        )
        self.get = to_raw_response_wrapper(
            metamessages.get,
        )


class AsyncMetamessagesResourceWithRawResponse:
    def __init__(self, metamessages: AsyncMetamessagesResource) -> None:
        self._metamessages = metamessages

        self.create = async_to_raw_response_wrapper(
            metamessages.create,
        )
        self.update = async_to_raw_response_wrapper(
            metamessages.update,
        )
        self.list = async_to_raw_response_wrapper(
            metamessages.list,
        )
        self.get = async_to_raw_response_wrapper(
            metamessages.get,
        )


class MetamessagesResourceWithStreamingResponse:
    def __init__(self, metamessages: MetamessagesResource) -> None:
        self._metamessages = metamessages

        self.create = to_streamed_response_wrapper(
            metamessages.create,
        )
        self.update = to_streamed_response_wrapper(
            metamessages.update,
        )
        self.list = to_streamed_response_wrapper(
            metamessages.list,
        )
        self.get = to_streamed_response_wrapper(
            metamessages.get,
        )


class AsyncMetamessagesResourceWithStreamingResponse:
    def __init__(self, metamessages: AsyncMetamessagesResource) -> None:
        self._metamessages = metamessages

        self.create = async_to_streamed_response_wrapper(
            metamessages.create,
        )
        self.update = async_to_streamed_response_wrapper(
            metamessages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            metamessages.list,
        )
        self.get = async_to_streamed_response_wrapper(
            metamessages.get,
        )
