# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.pagination import SyncPage, AsyncPage
from honcho.types.apps import User

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        user = client.apps.users.create(
            app_id="app_id",
            name="name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Honcho) -> None:
        user = client.apps.users.create(
            app_id="app_id",
            name="name",
            metadata={"foo": "bar"},
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.apps.users.with_raw_response.create(
            app_id="app_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.apps.users.with_streaming_response.create(
            app_id="app_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.with_raw_response.create(
                app_id="",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        user = client.apps.users.update(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        user = client.apps.users.update(
            user_id="user_id",
            app_id="app_id",
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.apps.users.with_raw_response.update(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.apps.users.with_streaming_response.update(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.with_raw_response.update(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.with_raw_response.update(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        user = client.apps.users.list(
            app_id="app_id",
        )
        assert_matches_type(SyncPage[User], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        user = client.apps.users.list(
            app_id="app_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(SyncPage[User], user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.apps.users.with_raw_response.list(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncPage[User], user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.apps.users.with_streaming_response.list(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncPage[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.with_raw_response.list(
                app_id="",
            )

    @parametrize
    def test_method_get(self, client: Honcho) -> None:
        user = client.apps.users.get(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Honcho) -> None:
        response = client.apps.users.with_raw_response.get(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Honcho) -> None:
        with client.apps.users.with_streaming_response.get(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.with_raw_response.get(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.with_raw_response.get(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    def test_method_get_by_name(self, client: Honcho) -> None:
        user = client.apps.users.get_by_name(
            name="name",
            app_id="app_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_get_by_name(self, client: Honcho) -> None:
        response = client.apps.users.with_raw_response.get_by_name(
            name="name",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_get_by_name(self, client: Honcho) -> None:
        with client.apps.users.with_streaming_response.get_by_name(
            name="name",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_name(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.with_raw_response.get_by_name(
                name="name",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.apps.users.with_raw_response.get_by_name(
                name="",
                app_id="app_id",
            )

    @parametrize
    def test_method_get_or_create(self, client: Honcho) -> None:
        user = client.apps.users.get_or_create(
            name="name",
            app_id="app_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_get_or_create(self, client: Honcho) -> None:
        response = client.apps.users.with_raw_response.get_or_create(
            name="name",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_get_or_create(self, client: Honcho) -> None:
        with client.apps.users.with_streaming_response.get_or_create(
            name="name",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_or_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.with_raw_response.get_or_create(
                name="name",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.apps.users.with_raw_response.get_or_create(
                name="",
                app_id="app_id",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.create(
            app_id="app_id",
            name="name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.create(
            app_id="app_id",
            name="name",
            metadata={"foo": "bar"},
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.with_raw_response.create(
            app_id="app_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.with_streaming_response.create(
            app_id="app_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.with_raw_response.create(
                app_id="",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.update(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.update(
            user_id="user_id",
            app_id="app_id",
            metadata={"foo": "bar"},
            name="name",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.with_raw_response.update(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.with_streaming_response.update(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.with_raw_response.update(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.with_raw_response.update(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.list(
            app_id="app_id",
        )
        assert_matches_type(AsyncPage[User], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.list(
            app_id="app_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[User], user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.with_raw_response.list(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncPage[User], user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.with_streaming_response.list(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncPage[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.with_raw_response.list(
                app_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.get(
            user_id="user_id",
            app_id="app_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.with_raw_response.get(
            user_id="user_id",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.with_streaming_response.get(
            user_id="user_id",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.with_raw_response.get(
                user_id="user_id",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.with_raw_response.get(
                user_id="",
                app_id="app_id",
            )

    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.get_by_name(
            name="name",
            app_id="app_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.with_raw_response.get_by_name(
            name="name",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.with_streaming_response.get_by_name(
            name="name",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.with_raw_response.get_by_name(
                name="name",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.apps.users.with_raw_response.get_by_name(
                name="",
                app_id="app_id",
            )

    @parametrize
    async def test_method_get_or_create(self, async_client: AsyncHoncho) -> None:
        user = await async_client.apps.users.get_or_create(
            name="name",
            app_id="app_id",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.with_raw_response.get_or_create(
            name="name",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_get_or_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.with_streaming_response.get_or_create(
            name="name",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_or_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.with_raw_response.get_or_create(
                name="name",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.apps.users.with_raw_response.get_or_create(
                name="",
                app_id="app_id",
            )
