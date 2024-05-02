# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.types.apps.users.sessions import (
    Metamessage,
    PageMetamessage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetamessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        metamessage = client.apps.users.sessions.metamessages.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Honcho) -> None:
        metamessage = client.apps.users.sessions.metamessages.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
            metadata={},
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.apps.users.sessions.metamessages.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.apps.users.sessions.metamessages.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content="string",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metamessage_type="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                content="string",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metamessage_type="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.create(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content="string",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metamessage_type="string",
            )

    @parametrize
    def test_method_retrieve(self, client: Honcho) -> None:
        metamessage = client.apps.users.sessions.metamessages.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Honcho) -> None:
        response = client.apps.users.sessions.metamessages.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Honcho) -> None:
        with client.apps.users.sessions.metamessages.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.retrieve(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.retrieve(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.retrieve(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metamessage_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.retrieve(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        metamessage = client.apps.users.sessions.metamessages.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        metamessage = client.apps.users.sessions.metamessages.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={},
            metamessage_type="string",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.apps.users.sessions.metamessages.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.apps.users.sessions.metamessages.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metamessage_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.update(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        metamessage = client.apps.users.sessions.metamessages.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageMetamessage, metamessage, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        metamessage = client.apps.users.sessions.metamessages.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
            page=1,
            reverse=True,
            size=1,
        )
        assert_matches_type(PageMetamessage, metamessage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.apps.users.sessions.metamessages.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = response.parse()
        assert_matches_type(PageMetamessage, metamessage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.apps.users.sessions.metamessages.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = response.parse()
            assert_matches_type(PageMetamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.list(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.list(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.apps.users.sessions.metamessages.with_raw_response.list(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncMetamessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.sessions.metamessages.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.sessions.metamessages.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
            metadata={},
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.metamessages.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = await response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.metamessages.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = await response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content="string",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metamessage_type="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                content="string",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metamessage_type="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.create(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content="string",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metamessage_type="string",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.sessions.metamessages.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.metamessages.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = await response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.metamessages.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = await response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.retrieve(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.retrieve(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.retrieve(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metamessage_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.retrieve(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.sessions.metamessages.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.sessions.metamessages.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={},
            metamessage_type="string",
        )
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.metamessages.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = await response.parse()
        assert_matches_type(Metamessage, metamessage, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.metamessages.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = await response.parse()
            assert_matches_type(Metamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `metamessage_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.update(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.sessions.metamessages.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PageMetamessage, metamessage, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        metamessage = await async_client.apps.users.sessions.metamessages.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="string",
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metamessage_type="string",
            page=1,
            reverse=True,
            size=1,
        )
        assert_matches_type(PageMetamessage, metamessage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.sessions.metamessages.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metamessage = await response.parse()
        assert_matches_type(PageMetamessage, metamessage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.sessions.metamessages.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metamessage = await response.parse()
            assert_matches_type(PageMetamessage, metamessage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.list(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.list(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.apps.users.sessions.metamessages.with_raw_response.list(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )