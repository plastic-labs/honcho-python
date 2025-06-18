# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.pagination import SyncPage, AsyncPage
from honcho.types.workspaces import (
    Peer,
    PeerChatResponse,
    PeerWorkingRepresentationResponse,
)
from honcho.types.workspaces.sessions import Message

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        peer = client.workspaces.peers.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
            feature_flags={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(Peer, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.update(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.update(
                peer_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        peer = client.workspaces.peers.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.list(
            workspace_id="workspace_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(SyncPage[Peer], peer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(SyncPage[Peer], peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_chat(self, client: Honcho) -> None:
        peer = client.workspaces.peers.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            queries="string",
        )
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    def test_method_chat_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            queries="string",
            session_id="session_id",
            stream=True,
            target="target",
        )
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    def test_raw_response_chat(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            queries="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    def test_streaming_response_chat(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            queries="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(PeerChatResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_chat(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.chat(
                peer_id="peer_id",
                workspace_id="",
                queries="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.chat(
                peer_id="",
                workspace_id="workspace_id",
                queries="string",
            )

    @parametrize
    def test_method_get_or_create(self, client: Honcho) -> None:
        peer = client.workspaces.peers.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_method_get_or_create_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.get_or_create(
            workspace_id="workspace_id",
            id="id",
            feature_flags={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_raw_response_get_or_create(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    def test_streaming_response_get_or_create(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(Peer, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_or_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.get_or_create(
                workspace_id="",
                id="id",
            )

    @parametrize
    def test_method_search(self, client: Honcho) -> None:
        peer = client.workspaces.peers.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            body="body",
        )
        assert_matches_type(SyncPage[Message], peer, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            body="body",
            page=1,
            size=1,
        )
        assert_matches_type(SyncPage[Message], peer, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(SyncPage[Message], peer, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(SyncPage[Message], peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.search(
                peer_id="peer_id",
                workspace_id="",
                body="body",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.search(
                peer_id="",
                workspace_id="workspace_id",
                body="body",
            )

    @parametrize
    def test_method_working_representation(self, client: Honcho) -> None:
        peer = client.workspaces.peers.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    def test_method_working_representation_with_all_params(self, client: Honcho) -> None:
        peer = client.workspaces.peers.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
            target="target",
        )
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    def test_raw_response_working_representation(self, client: Honcho) -> None:
        response = client.workspaces.peers.with_raw_response.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = response.parse()
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    def test_streaming_response_working_representation(self, client: Honcho) -> None:
        with client.workspaces.peers.with_streaming_response.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = response.parse()
            assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_working_representation(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.peers.with_raw_response.working_representation(
                peer_id="peer_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.workspaces.peers.with_raw_response.working_representation(
                peer_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )


class TestAsyncPeers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
            feature_flags={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.update(
            peer_id="peer_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(Peer, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.update(
                peer_id="peer_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.update(
                peer_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.list(
            workspace_id="workspace_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(AsyncPage[Peer], peer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(AsyncPage[Peer], peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_chat(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            queries="string",
        )
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            queries="string",
            session_id="session_id",
            stream=True,
            target="target",
        )
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            queries="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(PeerChatResponse, peer, path=["response"])

    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.chat(
            peer_id="peer_id",
            workspace_id="workspace_id",
            queries="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(PeerChatResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_chat(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.chat(
                peer_id="peer_id",
                workspace_id="",
                queries="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.chat(
                peer_id="",
                workspace_id="workspace_id",
                queries="string",
            )

    @parametrize
    async def test_method_get_or_create(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_method_get_or_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.get_or_create(
            workspace_id="workspace_id",
            id="id",
            feature_flags={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_raw_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(Peer, peer, path=["response"])

    @parametrize
    async def test_streaming_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.get_or_create(
            workspace_id="workspace_id",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(Peer, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_or_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.get_or_create(
                workspace_id="",
                id="id",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            body="body",
        )
        assert_matches_type(AsyncPage[Message], peer, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            body="body",
            page=1,
            size=1,
        )
        assert_matches_type(AsyncPage[Message], peer, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(AsyncPage[Message], peer, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.search(
            peer_id="peer_id",
            workspace_id="workspace_id",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(AsyncPage[Message], peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.search(
                peer_id="peer_id",
                workspace_id="",
                body="body",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.search(
                peer_id="",
                workspace_id="workspace_id",
                body="body",
            )

    @parametrize
    async def test_method_working_representation(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    async def test_method_working_representation_with_all_params(self, async_client: AsyncHoncho) -> None:
        peer = await async_client.workspaces.peers.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
            target="target",
        )
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    async def test_raw_response_working_representation(self, async_client: AsyncHoncho) -> None:
        response = await async_client.workspaces.peers.with_raw_response.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        peer = await response.parse()
        assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

    @parametrize
    async def test_streaming_response_working_representation(self, async_client: AsyncHoncho) -> None:
        async with async_client.workspaces.peers.with_streaming_response.working_representation(
            peer_id="peer_id",
            workspace_id="workspace_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            peer = await response.parse()
            assert_matches_type(PeerWorkingRepresentationResponse, peer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_working_representation(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.working_representation(
                peer_id="peer_id",
                workspace_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.workspaces.peers.with_raw_response.working_representation(
                peer_id="",
                workspace_id="workspace_id",
                session_id="session_id",
            )
