# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.pagination import SyncPage, AsyncPage
from honcho.types.apps.users import (
    Collection,
    CollectionQueryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        collection = client.apps.users.collections.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Honcho) -> None:
        collection = client.apps.users.collections.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            metadata={},
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.apps.users.collections.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.apps.users.collections.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                name="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.with_raw_response.create(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="string",
            )

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        collection = client.apps.users.collections.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        collection = client.apps.users.collections.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            metadata={},
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.apps.users.collections.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.apps.users.collections.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                name="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.with_raw_response.update(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="string",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        collection = client.apps.users.collections.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPage[Collection], collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        collection = client.apps.users.collections.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="string",
            page=1,
            reverse=True,
            size=1,
        )
        assert_matches_type(SyncPage[Collection], collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.apps.users.collections.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(SyncPage[Collection], collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.apps.users.collections.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(SyncPage[Collection], collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.with_raw_response.list(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.with_raw_response.list(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_delete(self, client: Honcho) -> None:
        collection = client.apps.users.collections.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Honcho) -> None:
        response = client.apps.users.collections.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Honcho) -> None:
        with client.apps.users.collections.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.with_raw_response.delete(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get(self, client: Honcho) -> None:
        collection = client.apps.users.collections.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Honcho) -> None:
        response = client.apps.users.collections.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Honcho) -> None:
        with client.apps.users.collections.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.with_raw_response.get(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get_by_name(self, client: Honcho) -> None:
        collection = client.apps.users.collections.get_by_name(
            "string",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_get_by_name(self, client: Honcho) -> None:
        response = client.apps.users.collections.with_raw_response.get_by_name(
            "string",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_get_by_name(self, client: Honcho) -> None:
        with client.apps.users.collections.with_streaming_response.get_by_name(
            "string",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_name(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.with_raw_response.get_by_name(
                "string",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.with_raw_response.get_by_name(
                "string",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.apps.users.collections.with_raw_response.get_by_name(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_query(self, client: Honcho) -> None:
        collection = client.apps.users.collections.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        )
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Honcho) -> None:
        collection = client.apps.users.collections.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
            filter="string",
            top_k=0,
        )
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Honcho) -> None:
        response = client.apps.users.collections.with_raw_response.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Honcho) -> None:
        with client.apps.users.collections.with_streaming_response.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionQueryResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.with_raw_response.query(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.with_raw_response.query(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                query="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.with_raw_response.query(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="string",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            metadata={},
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                name="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.create(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="string",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            metadata={},
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                name="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.update(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPage[Collection], collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="string",
            page=1,
            reverse=True,
            size=1,
        )
        assert_matches_type(AsyncPage[Collection], collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(AsyncPage[Collection], collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(AsyncPage[Collection], collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.list(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.list(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(object, collection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(object, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.delete(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.get(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.get_by_name(
            "string",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.with_raw_response.get_by_name(
            "string",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.with_streaming_response.get_by_name(
            "string",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.get_by_name(
                "string",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.get_by_name(
                "string",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.apps.users.collections.with_raw_response.get_by_name(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        )
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncHoncho) -> None:
        collection = await async_client.apps.users.collections.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
            filter="string",
            top_k=0,
        )
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.with_raw_response.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.with_streaming_response.query(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionQueryResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.query(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.query(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
                query="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.with_raw_response.query(
                "",
                app_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="string",
            )
