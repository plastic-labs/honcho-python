# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...types import (
    workspace_list_params,
    workspace_search_params,
    workspace_update_params,
    workspace_get_or_create_params,
    workspace_deriver_status_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .peers.peers import (
    PeersResource,
    AsyncPeersResource,
    PeersResourceWithRawResponse,
    AsyncPeersResourceWithRawResponse,
    PeersResourceWithStreamingResponse,
    AsyncPeersResourceWithStreamingResponse,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workspace import Workspace
from .sessions.sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ...types.deriver_status import DeriverStatus
from ...types.workspace_search_response import WorkspaceSearchResponse

__all__ = ["WorkspacesResource", "AsyncWorkspacesResource"]


class WorkspacesResource(SyncAPIResource):
    @cached_property
    def peers(self) -> PeersResource:
        return PeersResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return WorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return WorkspacesResourceWithStreamingResponse(self)

    def update(
        self,
        workspace_id: str,
        *,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workspace:
        """
        Update a Workspace

        Args:
          workspace_id: ID of the workspace to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._put(
            f"/v2/workspaces/{workspace_id}",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                },
                workspace_update_params.WorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        filter: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Workspace]:
        """
        Get all Workspaces

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/workspaces/list",
            page=SyncPage[Workspace],
            body=maybe_transform({"filter": filter}, workspace_list_params.WorkspaceListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    workspace_list_params.WorkspaceListParams,
                ),
            ),
            model=Workspace,
            method="post",
        )

    def deriver_status(
        self,
        workspace_id: str,
        *,
        observer_id: Optional[str] | NotGiven = NOT_GIVEN,
        sender_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeriverStatus:
        """
        Get the deriver processing status, optionally scoped to an observer, sender,
        and/or session

        Args:
          workspace_id: ID of the workspace

          observer_id: Optional observer ID to filter by

          sender_id: Optional sender ID to filter by

          session_id: Optional session ID to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            f"/v2/workspaces/{workspace_id}/deriver/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "observer_id": observer_id,
                        "sender_id": sender_id,
                        "session_id": session_id,
                    },
                    workspace_deriver_status_params.WorkspaceDeriverStatusParams,
                ),
            ),
            cast_to=DeriverStatus,
        )

    def get_or_create(
        self,
        *,
        id: str,
        configuration: Dict[str, object] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workspace:
        """
        Get a Workspace by ID.

        If workspace_id is provided as a query parameter, it uses that (must match JWT
        workspace_id). Otherwise, it uses the workspace_id from the JWT token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/workspaces",
            body=maybe_transform(
                {
                    "id": id,
                    "configuration": configuration,
                    "metadata": metadata,
                },
                workspace_get_or_create_params.WorkspaceGetOrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def search(
        self,
        workspace_id: str,
        *,
        query: str,
        filters: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceSearchResponse:
        """
        Search a Workspace

        Args:
          workspace_id: ID of the workspace to search

          query: Search query

          filters: Filters to scope the search

          limit: Number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            f"/v2/workspaces/{workspace_id}/search",
            body=maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "limit": limit,
                },
                workspace_search_params.WorkspaceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSearchResponse,
        )


class AsyncWorkspacesResource(AsyncAPIResource):
    @cached_property
    def peers(self) -> AsyncPeersResource:
        return AsyncPeersResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/plastic-labs/honcho-python-core#with_streaming_response
        """
        return AsyncWorkspacesResourceWithStreamingResponse(self)

    async def update(
        self,
        workspace_id: str,
        *,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workspace:
        """
        Update a Workspace

        Args:
          workspace_id: ID of the workspace to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._put(
            f"/v2/workspaces/{workspace_id}",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                },
                workspace_update_params.WorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        filter: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Workspace, AsyncPage[Workspace]]:
        """
        Get all Workspaces

        Args:
          page: Page number

          size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/workspaces/list",
            page=AsyncPage[Workspace],
            body=maybe_transform({"filter": filter}, workspace_list_params.WorkspaceListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "size": size,
                    },
                    workspace_list_params.WorkspaceListParams,
                ),
            ),
            model=Workspace,
            method="post",
        )

    async def deriver_status(
        self,
        workspace_id: str,
        *,
        observer_id: Optional[str] | NotGiven = NOT_GIVEN,
        sender_id: Optional[str] | NotGiven = NOT_GIVEN,
        session_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeriverStatus:
        """
        Get the deriver processing status, optionally scoped to an observer, sender,
        and/or session

        Args:
          workspace_id: ID of the workspace

          observer_id: Optional observer ID to filter by

          sender_id: Optional sender ID to filter by

          session_id: Optional session ID to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            f"/v2/workspaces/{workspace_id}/deriver/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "observer_id": observer_id,
                        "sender_id": sender_id,
                        "session_id": session_id,
                    },
                    workspace_deriver_status_params.WorkspaceDeriverStatusParams,
                ),
            ),
            cast_to=DeriverStatus,
        )

    async def get_or_create(
        self,
        *,
        id: str,
        configuration: Dict[str, object] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workspace:
        """
        Get a Workspace by ID.

        If workspace_id is provided as a query parameter, it uses that (must match JWT
        workspace_id). Otherwise, it uses the workspace_id from the JWT token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/workspaces",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "configuration": configuration,
                    "metadata": metadata,
                },
                workspace_get_or_create_params.WorkspaceGetOrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    async def search(
        self,
        workspace_id: str,
        *,
        query: str,
        filters: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkspaceSearchResponse:
        """
        Search a Workspace

        Args:
          workspace_id: ID of the workspace to search

          query: Search query

          filters: Filters to scope the search

          limit: Number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            f"/v2/workspaces/{workspace_id}/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "filters": filters,
                    "limit": limit,
                },
                workspace_search_params.WorkspaceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSearchResponse,
        )


class WorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.update = to_raw_response_wrapper(
            workspaces.update,
        )
        self.list = to_raw_response_wrapper(
            workspaces.list,
        )
        self.deriver_status = to_raw_response_wrapper(
            workspaces.deriver_status,
        )
        self.get_or_create = to_raw_response_wrapper(
            workspaces.get_or_create,
        )
        self.search = to_raw_response_wrapper(
            workspaces.search,
        )

    @cached_property
    def peers(self) -> PeersResourceWithRawResponse:
        return PeersResourceWithRawResponse(self._workspaces.peers)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._workspaces.sessions)


class AsyncWorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.update = async_to_raw_response_wrapper(
            workspaces.update,
        )
        self.list = async_to_raw_response_wrapper(
            workspaces.list,
        )
        self.deriver_status = async_to_raw_response_wrapper(
            workspaces.deriver_status,
        )
        self.get_or_create = async_to_raw_response_wrapper(
            workspaces.get_or_create,
        )
        self.search = async_to_raw_response_wrapper(
            workspaces.search,
        )

    @cached_property
    def peers(self) -> AsyncPeersResourceWithRawResponse:
        return AsyncPeersResourceWithRawResponse(self._workspaces.peers)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._workspaces.sessions)


class WorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.update = to_streamed_response_wrapper(
            workspaces.update,
        )
        self.list = to_streamed_response_wrapper(
            workspaces.list,
        )
        self.deriver_status = to_streamed_response_wrapper(
            workspaces.deriver_status,
        )
        self.get_or_create = to_streamed_response_wrapper(
            workspaces.get_or_create,
        )
        self.search = to_streamed_response_wrapper(
            workspaces.search,
        )

    @cached_property
    def peers(self) -> PeersResourceWithStreamingResponse:
        return PeersResourceWithStreamingResponse(self._workspaces.peers)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._workspaces.sessions)


class AsyncWorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.update = async_to_streamed_response_wrapper(
            workspaces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workspaces.list,
        )
        self.deriver_status = async_to_streamed_response_wrapper(
            workspaces.deriver_status,
        )
        self.get_or_create = async_to_streamed_response_wrapper(
            workspaces.get_or_create,
        )
        self.search = async_to_streamed_response_wrapper(
            workspaces.search,
        )

    @cached_property
    def peers(self) -> AsyncPeersResourceWithStreamingResponse:
        return AsyncPeersResourceWithStreamingResponse(self._workspaces.peers)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._workspaces.sessions)
