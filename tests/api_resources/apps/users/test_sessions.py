# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.pagination import SyncPage, AsyncPage
from honcho.types.apps.users import (
    Session,
    DialecticResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        session = client.apps.users.sessions.create(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Honcho) -> None:
        session = client.apps.users.sessions.create(
            user_id="user_id",
            app_id="app_id",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.apps.users.sessions.with_raw_response.create(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.apps.users.sessions.with_streaming_response.create(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.with_raw_response.create(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.with_raw_response.create(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        session = client.apps.users.sessions.update(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.apps.users.sessions.with_raw_response.update(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            metadata={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.apps.users.sessions.with_streaming_response.update(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            metadata={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.with_raw_response.update(
                session_id="session_id",
                app_id="",
                user_id="user_id",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.with_raw_response.update(
                session_id="session_id",
                app_id="app_id",
                user_id="",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.with_raw_response.update(
                session_id="",
                app_id="app_id",
                user_id="user_id",
                metadata={"foo": "bar"},
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        session = client.apps.users.sessions.list(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        session = client.apps.users.sessions.list(
            user_id="user_id",
            app_id="app_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
            is_active=True,
        )
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.apps.users.sessions.with_raw_response.list(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SyncPage[Session], session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.apps.users.sessions.with_streaming_response.list(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SyncPage[Session], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.with_raw_response.list(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.with_raw_response.list(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    def test_method_delete(self, client: Honcho) -> None:
        session = client.apps.users.sessions.delete(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(object, session, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Honcho) -> None:
        response = client.apps.users.sessions.with_raw_response.delete(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(object, session, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Honcho) -> None:
        with client.apps.users.sessions.with_streaming_response.delete(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(object, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.with_raw_response.delete(
                session_id="session_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.with_raw_response.delete(
                session_id="session_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.with_raw_response.delete(
                session_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    def test_method_chat(self, client: Honcho) -> None:
        session = client.apps.users.sessions.chat(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            queries="string",
        )
        assert_matches_type(DialecticResponse, session, path=["response"])

    @parametrize
    def test_method_chat_with_all_params(self, client: Honcho) -> None:
        session = client.apps.users.sessions.chat(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            queries="string",
            stream=True,
        )
        assert_matches_type(DialecticResponse, session, path=["response"])

    @parametrize
    def test_raw_response_chat(self, client: Honcho) -> None:
        response = client.apps.users.sessions.with_raw_response.chat(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            queries="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(DialecticResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_chat(self, client: Honcho) -> None:
        with client.apps.users.sessions.with_streaming_response.chat(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            queries="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(DialecticResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_chat(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.with_raw_response.chat(
                session_id="session_id",
                app_id="",
                user_id="user_id",
                queries="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.with_raw_response.chat(
                session_id="session_id",
                app_id="app_id",
                user_id="",
                queries="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.with_raw_response.chat(
                session_id="",
                app_id="app_id",
                user_id="user_id",
                queries="string",
            )

    @parametrize
    def test_method_clone(self, client: Honcho) -> None:
        session = client.apps.users.sessions.clone(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_method_clone_with_all_params(self, client: Honcho) -> None:
        session = client.apps.users.sessions.clone(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            deep_copy=True,
            message_id="message_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_clone(self, client: Honcho) -> None:
        response = client.apps.users.sessions.with_raw_response.clone(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_clone(self, client: Honcho) -> None:
        with client.apps.users.sessions.with_streaming_response.clone(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clone(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.with_raw_response.clone(
                session_id="session_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.with_raw_response.clone(
                session_id="session_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.with_raw_response.clone(
                session_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    def test_method_get(self, client: Honcho) -> None:
        session = client.apps.users.sessions.get(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Honcho) -> None:
        session = client.apps.users.sessions.get(
            user_id="user_id",
            app_id="app_id",
            session_id="session_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Honcho) -> None:
        response = client.apps.users.sessions.with_raw_response.get(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Honcho) -> None:
        with client.apps.users.sessions.with_streaming_response.get(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.with_raw_response.get(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.with_raw_response.get(
                user_id="",
                app_id="app_id",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.create(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.create(
            user_id="user_id",
            app_id="app_id",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.with_raw_response.create(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.with_streaming_response.create(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.create(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.create(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.update(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.with_raw_response.update(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            metadata={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.with_streaming_response.update(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            metadata={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.update(
                session_id="session_id",
                app_id="",
                user_id="user_id",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.update(
                session_id="session_id",
                app_id="app_id",
                user_id="",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.update(
                session_id="",
                app_id="app_id",
                user_id="user_id",
                metadata={"foo": "bar"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.list(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.list(
            user_id="user_id",
            app_id="app_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
            is_active=True,
        )
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.with_raw_response.list(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AsyncPage[Session], session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.with_streaming_response.list(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AsyncPage[Session], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.list(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.list(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.delete(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(object, session, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.with_raw_response.delete(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(object, session, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.with_streaming_response.delete(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(object, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.delete(
                session_id="session_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.delete(
                session_id="session_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.delete(
                session_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    async def test_method_chat(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.chat(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            queries="string",
        )
        assert_matches_type(DialecticResponse, session, path=["response"])

    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.chat(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            queries="string",
            stream=True,
        )
        assert_matches_type(DialecticResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.with_raw_response.chat(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            queries="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(DialecticResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.with_streaming_response.chat(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            queries="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(DialecticResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_chat(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.chat(
                session_id="session_id",
                app_id="",
                user_id="user_id",
                queries="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.chat(
                session_id="session_id",
                app_id="app_id",
                user_id="",
                queries="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.chat(
                session_id="",
                app_id="app_id",
                user_id="user_id",
                queries="string",
            )

    @parametrize
    async def test_method_clone(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.clone(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.clone(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            deep_copy=True,
            message_id="message_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.with_raw_response.clone(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.with_streaming_response.clone(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clone(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.clone(
                session_id="session_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.clone(
                session_id="session_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.clone(
                session_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.get(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHoncho) -> None:
        session = await async_client.apps.users.sessions.get(
            user_id="user_id",
            app_id="app_id",
            session_id="session_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.with_raw_response.get(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.with_streaming_response.get(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.get(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.with_raw_response.get(
                user_id="",
                app_id="app_id",
            )
