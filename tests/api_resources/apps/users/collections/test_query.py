# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.types.apps.users.collections import QueryQueryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_query(self, client: Honcho) -> None:
        query = client.apps.users.collections.query.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        )
        assert_matches_type(QueryQueryResponse, query, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Honcho) -> None:
        query = client.apps.users.collections.query.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
            filter="string",
            top_k=0,
        )
        assert_matches_type(QueryQueryResponse, query, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Honcho) -> None:
        response = client.apps.users.collections.query.with_raw_response.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryQueryResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Honcho) -> None:
        with client.apps.users.collections.query.with_streaming_response.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryQueryResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.query.with_raw_response.query(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.query.with_raw_response.query(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                query="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.query.with_raw_response.query(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="string",
            )


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_query(self, async_client: AsyncHoncho) -> None:
        query = await async_client.apps.users.collections.query.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        )
        assert_matches_type(QueryQueryResponse, query, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncHoncho) -> None:
        query = await async_client.apps.users.collections.query.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
            filter="string",
            top_k=0,
        )
        assert_matches_type(QueryQueryResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.query.with_raw_response.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryQueryResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.query.with_streaming_response.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryQueryResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.query.with_raw_response.query(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.query.with_raw_response.query(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                query="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.query.with_raw_response.query(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="string",
            )
