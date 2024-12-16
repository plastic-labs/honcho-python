# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.pagination import SyncPage, AsyncPage
from honcho.types.apps.users.sessions import (
    Message,
    MessageBatchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        message = client.apps.users.sessions.messages.create(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            content="content",
            is_user=True,
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Honcho) -> None:
        message = client.apps.users.sessions.messages.create(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            content="content",
            is_user=True,
            metadata={"foo": "bar"},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.apps.users.sessions.messages.with_raw_response.create(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            content="content",
            is_user=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.apps.users.sessions.messages.with_streaming_response.create(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            content="content",
            is_user=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.create(
                session_id="session_id",
                app_id="",
                user_id="user_id",
                content="content",
                is_user=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.create(
                session_id="session_id",
                app_id="app_id",
                user_id="",
                content="content",
                is_user=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.create(
                session_id="",
                app_id="app_id",
                user_id="user_id",
                content="content",
                is_user=True,
            )

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        message = client.apps.users.sessions.messages.update(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.apps.users.sessions.messages.with_raw_response.update(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
            metadata={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.apps.users.sessions.messages.with_streaming_response.update(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
            metadata={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.update(
                message_id="message_id",
                app_id="",
                user_id="user_id",
                session_id="session_id",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.update(
                message_id="message_id",
                app_id="app_id",
                user_id="",
                session_id="session_id",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.update(
                message_id="message_id",
                app_id="app_id",
                user_id="user_id",
                session_id="",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.update(
                message_id="",
                app_id="app_id",
                user_id="user_id",
                session_id="session_id",
                metadata={"foo": "bar"},
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        message = client.apps.users.sessions.messages.list(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(SyncPage[Message], message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        message = client.apps.users.sessions.messages.list(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Message], message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.apps.users.sessions.messages.with_raw_response.list(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncPage[Message], message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.apps.users.sessions.messages.with_streaming_response.list(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncPage[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.list(
                session_id="session_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.list(
                session_id="session_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.list(
                session_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    def test_method_batch(self, client: Honcho) -> None:
        message = client.apps.users.sessions.messages.batch(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            messages=[
                {
                    "content": "content",
                    "is_user": True,
                }
            ],
        )
        assert_matches_type(MessageBatchResponse, message, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: Honcho) -> None:
        response = client.apps.users.sessions.messages.with_raw_response.batch(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            messages=[
                {
                    "content": "content",
                    "is_user": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageBatchResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: Honcho) -> None:
        with client.apps.users.sessions.messages.with_streaming_response.batch(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            messages=[
                {
                    "content": "content",
                    "is_user": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageBatchResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_batch(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.batch(
                session_id="session_id",
                app_id="",
                user_id="user_id",
                messages=[
                    {
                        "content": "content",
                        "is_user": True,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.batch(
                session_id="session_id",
                app_id="app_id",
                user_id="",
                messages=[
                    {
                        "content": "content",
                        "is_user": True,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.batch(
                session_id="",
                app_id="app_id",
                user_id="user_id",
                messages=[
                    {
                        "content": "content",
                        "is_user": True,
                    }
                ],
            )

    @parametrize
    def test_method_get(self, client: Honcho) -> None:
        message = client.apps.users.sessions.messages.get(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Honcho) -> None:
        response = client.apps.users.sessions.messages.with_raw_response.get(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Honcho) -> None:
        with client.apps.users.sessions.messages.with_streaming_response.get(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.get(
                message_id="message_id",
                app_id="",
                user_id="user_id",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.get(
                message_id="message_id",
                app_id="app_id",
                user_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.get(
                message_id="message_id",
                app_id="app_id",
                user_id="user_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.apps.users.sessions.messages.with_raw_response.get(
                message_id="",
                app_id="app_id",
                user_id="user_id",
                session_id="session_id",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        message = await async_client.apps.users.sessions.messages.create(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            content="content",
            is_user=True,
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        message = await async_client.apps.users.sessions.messages.create(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            content="content",
            is_user=True,
            metadata={"foo": "bar"},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.messages.with_raw_response.create(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            content="content",
            is_user=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.messages.with_streaming_response.create(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            content="content",
            is_user=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.create(
                session_id="session_id",
                app_id="",
                user_id="user_id",
                content="content",
                is_user=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.create(
                session_id="session_id",
                app_id="app_id",
                user_id="",
                content="content",
                is_user=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.create(
                session_id="",
                app_id="app_id",
                user_id="user_id",
                content="content",
                is_user=True,
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        message = await async_client.apps.users.sessions.messages.update(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.messages.with_raw_response.update(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
            metadata={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.messages.with_streaming_response.update(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
            metadata={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.update(
                message_id="message_id",
                app_id="",
                user_id="user_id",
                session_id="session_id",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.update(
                message_id="message_id",
                app_id="app_id",
                user_id="",
                session_id="session_id",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.update(
                message_id="message_id",
                app_id="app_id",
                user_id="user_id",
                session_id="",
                metadata={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.update(
                message_id="",
                app_id="app_id",
                user_id="user_id",
                session_id="session_id",
                metadata={"foo": "bar"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        message = await async_client.apps.users.sessions.messages.list(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(AsyncPage[Message], message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        message = await async_client.apps.users.sessions.messages.list(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Message], message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.messages.with_raw_response.list(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncPage[Message], message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.messages.with_streaming_response.list(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncPage[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.list(
                session_id="session_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.list(
                session_id="session_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.list(
                session_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    async def test_method_batch(self, async_client: AsyncHoncho) -> None:
        message = await async_client.apps.users.sessions.messages.batch(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            messages=[
                {
                    "content": "content",
                    "is_user": True,
                }
            ],
        )
        assert_matches_type(MessageBatchResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.messages.with_raw_response.batch(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            messages=[
                {
                    "content": "content",
                    "is_user": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageBatchResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.messages.with_streaming_response.batch(
            session_id="session_id",
            app_id="app_id",
            user_id="user_id",
            messages=[
                {
                    "content": "content",
                    "is_user": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageBatchResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_batch(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.batch(
                session_id="session_id",
                app_id="",
                user_id="user_id",
                messages=[
                    {
                        "content": "content",
                        "is_user": True,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.batch(
                session_id="session_id",
                app_id="app_id",
                user_id="",
                messages=[
                    {
                        "content": "content",
                        "is_user": True,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.batch(
                session_id="",
                app_id="app_id",
                user_id="user_id",
                messages=[
                    {
                        "content": "content",
                        "is_user": True,
                    }
                ],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncHoncho) -> None:
        message = await async_client.apps.users.sessions.messages.get(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.messages.with_raw_response.get(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.messages.with_streaming_response.get(
            message_id="message_id",
            app_id="app_id",
            user_id="user_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.get(
                message_id="message_id",
                app_id="",
                user_id="user_id",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.get(
                message_id="message_id",
                app_id="app_id",
                user_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.get(
                message_id="message_id",
                app_id="app_id",
                user_id="user_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.apps.users.sessions.messages.with_raw_response.get(
                message_id="",
                app_id="app_id",
                user_id="user_id",
                session_id="session_id",
            )
