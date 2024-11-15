# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
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
from ....types.apps.users import metamessage_list_params
from ....types.apps.users.sessions.metamessage import Metamessage

__all__ = ["MetamessagesResource", "AsyncMetamessagesResource"]


class MetamessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetamessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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

    def list(
        self,
        user_id: str,
        *,
        app_id: str,
        page: int | NotGiven = NOT_GIVEN,
        reverse: Optional[bool] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        filter: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Metamessage]:
        """
        Paginate through the user metamessages for a user

        Args:
          page: Page number

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
                    "metamessage_type": metamessage_type,
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


class AsyncMetamessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetamessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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

    def list(
        self,
        user_id: str,
        *,
        app_id: str,
        page: int | NotGiven = NOT_GIVEN,
        reverse: Optional[bool] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        filter: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Metamessage, AsyncPage[Metamessage]]:
        """
        Paginate through the user metamessages for a user

        Args:
          page: Page number

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
                    "metamessage_type": metamessage_type,
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


class MetamessagesResourceWithRawResponse:
    def __init__(self, metamessages: MetamessagesResource) -> None:
        self._metamessages = metamessages

        self.list = to_raw_response_wrapper(
            metamessages.list,
        )


class AsyncMetamessagesResourceWithRawResponse:
    def __init__(self, metamessages: AsyncMetamessagesResource) -> None:
        self._metamessages = metamessages

        self.list = async_to_raw_response_wrapper(
            metamessages.list,
        )


class MetamessagesResourceWithStreamingResponse:
    def __init__(self, metamessages: MetamessagesResource) -> None:
        self._metamessages = metamessages

        self.list = to_streamed_response_wrapper(
            metamessages.list,
        )


class AsyncMetamessagesResourceWithStreamingResponse:
    def __init__(self, metamessages: AsyncMetamessagesResource) -> None:
        self._metamessages = metamessages

        self.list = async_to_streamed_response_wrapper(
            metamessages.list,
        )
