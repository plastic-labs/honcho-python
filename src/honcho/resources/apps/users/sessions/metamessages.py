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
from .....types.apps.users.sessions import (
    metamessage_list_params,
    metamessage_create_params,
    metamessage_update_params,
    metamessage_retrieve_params,
)
from .....types.apps.users.sessions.metamessage import Metamessage
from .....types.apps.users.sessions.page_metamessage import PageMetamessage

__all__ = ["MetamessagesResource", "AsyncMetamessagesResource"]


class MetamessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetamessagesResourceWithRawResponse:
        return MetamessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetamessagesResourceWithStreamingResponse:
        return MetamessagesResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        app_id: str,
        user_id: str,
        content: str,
        message_id: str,
        metamessage_type: str,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Adds a message to a session

        Args: app_id (uuid.UUID): The ID of the app representing the client application
        using honcho user_id (str): The User ID representing the user, managed by the
        user session_id (int): The ID of the Session to add the message to message
        (schemas.MessageCreate): The Message object to add containing the message
        content and type

        Returns: schemas.Message: The Message object of the added message

        Raises: HTTPException: If the session is not found

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages",
            body=maybe_transform(
                {
                    "content": content,
                    "message_id": message_id,
                    "metamessage_type": metamessage_type,
                    "metadata": metadata,
                },
                metamessage_create_params.MetamessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )

    def retrieve(
        self,
        metamessage_id: str,
        *,
        app_id: str,
        user_id: str,
        session_id: str,
        message_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Get a specific Metamessage by ID

        Args: app_id (uuid.UUID): The ID of the app representing the client application
        using honcho user_id (str): The User ID representing the user, managed by the
        user session_id (int): The ID of the Session to retrieve

        Returns: schemas.Session: The Session object of the requested Session

        Raises: HTTPException: If the session is not found

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not metamessage_id:
            raise ValueError(f"Expected a non-empty value for `metamessage_id` but received {metamessage_id!r}")
        return self._get(
            f"/apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages/{metamessage_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"message_id": message_id}, metamessage_retrieve_params.MetamessageRetrieveParams
                ),
            ),
            cast_to=Metamessage,
        )

    def update(
        self,
        metamessage_id: str,
        *,
        app_id: str,
        user_id: str,
        session_id: str,
        message_id: str,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Update's the metadata of a metamessage

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not metamessage_id:
            raise ValueError(f"Expected a non-empty value for `metamessage_id` but received {metamessage_id!r}")
        return self._put(
            f"/apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages/{metamessage_id}",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "metadata": metadata,
                    "metamessage_type": metamessage_type,
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
        session_id: str,
        *,
        app_id: str,
        user_id: str,
        filter: Optional[str] | NotGiven = NOT_GIVEN,
        message_id: Optional[str] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        reverse: Optional[bool] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageMetamessage:
        """
        Get all messages for a session

        Args: app_id (uuid.UUID): The ID of the app representing the client application
        using honcho user_id (str): The User ID representing the user, managed by the
        user session_id (int): The ID of the Session to retrieve reverse (bool): Whether
        to reverse the order of the metamessages

        Returns: list[schemas.Message]: List of Message objects

        Raises: HTTPException: If the session is not found

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "message_id": message_id,
                        "metamessage_type": metamessage_type,
                        "page": page,
                        "reverse": reverse,
                        "size": size,
                    },
                    metamessage_list_params.MetamessageListParams,
                ),
            ),
            cast_to=PageMetamessage,
        )


class AsyncMetamessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetamessagesResourceWithRawResponse:
        return AsyncMetamessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetamessagesResourceWithStreamingResponse:
        return AsyncMetamessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        app_id: str,
        user_id: str,
        content: str,
        message_id: str,
        metamessage_type: str,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Adds a message to a session

        Args: app_id (uuid.UUID): The ID of the app representing the client application
        using honcho user_id (str): The User ID representing the user, managed by the
        user session_id (int): The ID of the Session to add the message to message
        (schemas.MessageCreate): The Message object to add containing the message
        content and type

        Returns: schemas.Message: The Message object of the added message

        Raises: HTTPException: If the session is not found

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "message_id": message_id,
                    "metamessage_type": metamessage_type,
                    "metadata": metadata,
                },
                metamessage_create_params.MetamessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )

    async def retrieve(
        self,
        metamessage_id: str,
        *,
        app_id: str,
        user_id: str,
        session_id: str,
        message_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Get a specific Metamessage by ID

        Args: app_id (uuid.UUID): The ID of the app representing the client application
        using honcho user_id (str): The User ID representing the user, managed by the
        user session_id (int): The ID of the Session to retrieve

        Returns: schemas.Session: The Session object of the requested Session

        Raises: HTTPException: If the session is not found

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not metamessage_id:
            raise ValueError(f"Expected a non-empty value for `metamessage_id` but received {metamessage_id!r}")
        return await self._get(
            f"/apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages/{metamessage_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"message_id": message_id}, metamessage_retrieve_params.MetamessageRetrieveParams
                ),
            ),
            cast_to=Metamessage,
        )

    async def update(
        self,
        metamessage_id: str,
        *,
        app_id: str,
        user_id: str,
        session_id: str,
        message_id: str,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Metamessage:
        """
        Update's the metadata of a metamessage

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not metamessage_id:
            raise ValueError(f"Expected a non-empty value for `metamessage_id` but received {metamessage_id!r}")
        return await self._put(
            f"/apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages/{metamessage_id}",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "metadata": metadata,
                    "metamessage_type": metamessage_type,
                },
                metamessage_update_params.MetamessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metamessage,
        )

    async def list(
        self,
        session_id: str,
        *,
        app_id: str,
        user_id: str,
        filter: Optional[str] | NotGiven = NOT_GIVEN,
        message_id: Optional[str] | NotGiven = NOT_GIVEN,
        metamessage_type: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        reverse: Optional[bool] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageMetamessage:
        """
        Get all messages for a session

        Args: app_id (uuid.UUID): The ID of the app representing the client application
        using honcho user_id (str): The User ID representing the user, managed by the
        user session_id (int): The ID of the Session to retrieve reverse (bool): Whether
        to reverse the order of the metamessages

        Returns: list[schemas.Message]: List of Message objects

        Raises: HTTPException: If the session is not found

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
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "message_id": message_id,
                        "metamessage_type": metamessage_type,
                        "page": page,
                        "reverse": reverse,
                        "size": size,
                    },
                    metamessage_list_params.MetamessageListParams,
                ),
            ),
            cast_to=PageMetamessage,
        )


class MetamessagesResourceWithRawResponse:
    def __init__(self, metamessages: MetamessagesResource) -> None:
        self._metamessages = metamessages

        self.create = to_raw_response_wrapper(
            metamessages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            metamessages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            metamessages.update,
        )
        self.list = to_raw_response_wrapper(
            metamessages.list,
        )


class AsyncMetamessagesResourceWithRawResponse:
    def __init__(self, metamessages: AsyncMetamessagesResource) -> None:
        self._metamessages = metamessages

        self.create = async_to_raw_response_wrapper(
            metamessages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            metamessages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            metamessages.update,
        )
        self.list = async_to_raw_response_wrapper(
            metamessages.list,
        )


class MetamessagesResourceWithStreamingResponse:
    def __init__(self, metamessages: MetamessagesResource) -> None:
        self._metamessages = metamessages

        self.create = to_streamed_response_wrapper(
            metamessages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            metamessages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            metamessages.update,
        )
        self.list = to_streamed_response_wrapper(
            metamessages.list,
        )


class AsyncMetamessagesResourceWithStreamingResponse:
    def __init__(self, metamessages: AsyncMetamessagesResource) -> None:
        self._metamessages = metamessages

        self.create = async_to_streamed_response_wrapper(
            metamessages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            metamessages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            metamessages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            metamessages.list,
        )
