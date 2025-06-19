# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.pagination import SyncPage, AsyncPage
from honcho_core.types.workspaces import Session

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        session = client.workspaces.peers.sessions.list(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        session = client.workspaces.peers.sessions.list(
            peer_id="peer_id",
            workspace_id="workspace_id",
            page=1,
            size=1,
            filter={"foo": "bar"},
            is_active=True,
        )
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.peers.sessions.with_raw_response.list(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.peers.sessions.with_streaming_response.list(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SyncPage[Session], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.sessions.with_raw_response.list(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.sessions.with_raw_response.list(
                peer_id="",
                workspace_id="workspace_id",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.peers.sessions.list(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.workspaces.peers.sessions.list(
            peer_id="peer_id",
            workspace_id="workspace_id",
            page=1,
            size=1,
            filter={"foo": "bar"},
            is_active=True,
        )
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.sessions.with_raw_response.list(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.sessions.with_streaming_response.list(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AsyncPage[Session], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.sessions.with_raw_response.list(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.sessions.with_raw_response.list(
                peer_id="",
                workspace_id="workspace_id",
            )
