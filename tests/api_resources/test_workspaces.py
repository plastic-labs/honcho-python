# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core.types import (
    Workspace,
)
from honcho_core.pagination import SyncPage, AsyncPage
from honcho_core.types.workspaces.sessions import Message

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        workspace = client.workspaces.update(
            workspace_id="workspace_id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.update(
            workspace_id="workspace_id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.update(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.update(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.update(
                workspace_id="",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        workspace = client.workspaces.list()
        assert_matches_type(SyncPage[Workspace], workspace, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.list(
            page=1,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Workspace], workspace, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(SyncPage[Workspace], workspace, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(SyncPage[Workspace], workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_or_create(self, client: Honcho) -> None:
        workspace = client.workspaces.get_or_create(
            id="id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_method_get_or_create_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.get_or_create(
            id="id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_get_or_create(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.get_or_create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_get_or_create(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.get_or_create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Honcho) -> None:
        workspace = client.workspaces.search(
            workspace_id="workspace_id",
            body="body",
        )
        assert_matches_type(SyncPage[Message], workspace, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Honcho) -> None:
        workspace = client.workspaces.search(
            workspace_id="workspace_id",
            body="body",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[Message], workspace, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Honcho) -> None:
        response = client.workspaces.with_raw_response.search(
            workspace_id="workspace_id",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(SyncPage[Message], workspace, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Honcho) -> None:
        with client.workspaces.with_streaming_response.search(
            workspace_id="workspace_id",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(SyncPage[Message], workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.search(
                workspace_id="",
                body="body",
            )


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.update(
            workspace_id="workspace_id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.update(
            workspace_id="workspace_id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.update(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.update(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.update(
                workspace_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.list()
        assert_matches_type(AsyncPage[Workspace], workspace, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.list(
            page=1,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Workspace], workspace, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(AsyncPage[Workspace], workspace, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(AsyncPage[Workspace], workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_or_create(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.get_or_create(
            id="id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_method_get_or_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.get_or_create(
            id="id",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.get_or_create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.get_or_create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.search(
            workspace_id="workspace_id",
            body="body",
        )
        assert_matches_type(AsyncPage[Message], workspace, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHoncho) -> None:
        workspace = await async_client.workspaces.search(
            workspace_id="workspace_id",
            body="body",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[Message], workspace, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.with_raw_response.search(
            workspace_id="workspace_id",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(AsyncPage[Message], workspace, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.with_streaming_response.search(
            workspace_id="workspace_id",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(AsyncPage[Message], workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.search(
                workspace_id="",
                body="body",
            )
