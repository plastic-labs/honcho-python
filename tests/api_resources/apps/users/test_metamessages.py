# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.pagination import SyncPage, AsyncPage
from honcho.types.apps.users import (
    Metamessage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetamessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        metamessage = client.apps.users.metamessages.create(
            user_id="user_id",
            app_id="app_id",
            content="content",
            metamessage_type="x",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Honcho) -> None:
        metamessage = client.apps.users.metamessages.create(
            user_id="user_id",
            app_id="app_id",
            content="content",
            metamessage_type="x",
            message_id="message_id",
            metadata={"foo": "bar"},
            session_id="session_id",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.apps.users.metamessages.with_raw_response.create(
            user_id="user_id",
            app_id="app_id",
            content="content",
            metamessage_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.apps.users.metamessages.with_streaming_response.create(
            user_id="user_id",
            app_id="app_id",
            content="content",
            metamessage_type="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.create(
                user_id="user_id",
                app_id="",
                content="content",
                metamessage_type="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.create(
                user_id="",
                app_id="app_id",
                content="content",
                metamessage_type="x",
            )

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        metamessage = client.apps.users.metamessages.update(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        metamessage = client.apps.users.metamessages.update(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
            message_id="message_id",
            metadata={"foo": "bar"},
            metamessage_type="metamessage_type",
            session_id="session_id",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.apps.users.metamessages.with_raw_response.update(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.apps.users.metamessages.with_streaming_response.update(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.update(
                metamessage_id="metamessage_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.update(
                metamessage_id="metamessage_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metamessage_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.update(
                metamessage_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        metamessage = client.apps.users.metamessages.list(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(SyncPage[Metamessage], metamessage, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        metamessage = client.apps.users.metamessages.list(
            user_id="user_id",
            app_id="app_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
            message_id="message_id",
            metamessage_type="metamessage_type",
            session_id="session_id",
        )
        assert_matches_type(SyncPage[Metamessage], metamessage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.apps.users.metamessages.with_raw_response.list(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = response.parse()
        assert_matches_type(SyncPage[Metamessage], metamessage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.apps.users.metamessages.with_streaming_response.list(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = response.parse()
            assert_matches_type(SyncPage[Metamessage], metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.list(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.list(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    def test_method_get(self, client: Honcho) -> None:
        metamessage = client.apps.users.metamessages.get(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Honcho) -> None:
        response = client.apps.users.metamessages.with_raw_response.get(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Honcho) -> None:
        with client.apps.users.metamessages.with_streaming_response.get(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.get(
                metamessage_id="metamessage_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.get(
                metamessage_id="metamessage_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metamessage_id` but received ''"):
            client.apps.users.metamessages.with_raw_response.get(
                metamessage_id="",
                app_id="app_id",
                user_id="user_id",
            )


class TestAsyncMetamessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.metamessages.create(
            user_id="user_id",
            app_id="app_id",
            content="content",
            metamessage_type="x",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.metamessages.create(
            user_id="user_id",
            app_id="app_id",
            content="content",
            metamessage_type="x",
            message_id="message_id",
            metadata={"foo": "bar"},
            session_id="session_id",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.metamessages.with_raw_response.create(
            user_id="user_id",
            app_id="app_id",
            content="content",
            metamessage_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = await response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.metamessages.with_streaming_response.create(
            user_id="user_id",
            app_id="app_id",
            content="content",
            metamessage_type="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = await response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.create(
                user_id="user_id",
                app_id="",
                content="content",
                metamessage_type="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.create(
                user_id="",
                app_id="app_id",
                content="content",
                metamessage_type="x",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.metamessages.update(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.metamessages.update(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
            message_id="message_id",
            metadata={"foo": "bar"},
            metamessage_type="metamessage_type",
            session_id="session_id",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.metamessages.with_raw_response.update(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = await response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.metamessages.with_streaming_response.update(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = await response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.update(
                metamessage_id="metamessage_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.update(
                metamessage_id="metamessage_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metamessage_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.update(
                metamessage_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.metamessages.list(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(AsyncPage[Metamessage], metamessage, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.metamessages.list(
            user_id="user_id",
            app_id="app_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
            message_id="message_id",
            metamessage_type="metamessage_type",
            session_id="session_id",
        )
        assert_matches_type(AsyncPage[Metamessage], metamessage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.metamessages.with_raw_response.list(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = await response.parse()
        assert_matches_type(AsyncPage[Metamessage], metamessage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.metamessages.with_streaming_response.list(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = await response.parse()
            assert_matches_type(AsyncPage[Metamessage], metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.list(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.list(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.metamessages.get(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.metamessages.with_raw_response.get(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = await response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.metamessages.with_streaming_response.get(
            metamessage_id="metamessage_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = await response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.get(
                metamessage_id="metamessage_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.get(
                metamessage_id="metamessage_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metamessage_id` but received ''"):
            await async_client.apps.users.metamessages.with_raw_response.get(
                metamessage_id="",
                app_id="app_id",
                user_id="user_id",
            )
