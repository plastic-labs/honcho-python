# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.pagination import SyncPage, AsyncPage
from honcho.types.apps.users.collections import (
    Document,
    DocumentQueryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.create(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            content="x",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.create(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            content="x",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.apps.users.collections.documents.with_raw_response.create(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            content="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.apps.users.collections.documents.with_streaming_response.create(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            content="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.create(
                collection_id="collection_id",
                app_id="",
                user_id="user_id",
                content="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.create(
                collection_id="collection_id",
                app_id="app_id",
                user_id="",
                content="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.create(
                collection_id="",
                app_id="app_id",
                user_id="user_id",
                content="x",
            )

    @parametrize
    def test_method_update(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.update(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.update(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
            content="x",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Honcho) -> None:
        response = client.apps.users.collections.documents.with_raw_response.update(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Honcho) -> None:
        with client.apps.users.collections.documents.with_streaming_response.update(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.update(
                document_id="document_id",
                app_id="",
                user_id="user_id",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.update(
                document_id="document_id",
                app_id="app_id",
                user_id="",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.update(
                document_id="document_id",
                app_id="app_id",
                user_id="user_id",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.update(
                document_id="",
                app_id="app_id",
                user_id="user_id",
                collection_id="collection_id",
            )

    @parametrize
    def test_method_list(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.list(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(SyncPage[Document], document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.list(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(SyncPage[Document], document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Honcho) -> None:
        response = client.apps.users.collections.documents.with_raw_response.list(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(SyncPage[Document], document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Honcho) -> None:
        with client.apps.users.collections.documents.with_streaming_response.list(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(SyncPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.list(
                collection_id="collection_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.list(
                collection_id="collection_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.list(
                collection_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    def test_method_delete(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.delete(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )
        assert_matches_type(object, document, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Honcho) -> None:
        response = client.apps.users.collections.documents.with_raw_response.delete(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(object, document, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Honcho) -> None:
        with client.apps.users.collections.documents.with_streaming_response.delete(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(object, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.delete(
                document_id="document_id",
                app_id="",
                user_id="user_id",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.delete(
                document_id="document_id",
                app_id="app_id",
                user_id="",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.delete(
                document_id="document_id",
                app_id="app_id",
                user_id="user_id",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.delete(
                document_id="",
                app_id="app_id",
                user_id="user_id",
                collection_id="collection_id",
            )

    @parametrize
    def test_method_get(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.get(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Honcho) -> None:
        response = client.apps.users.collections.documents.with_raw_response.get(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Honcho) -> None:
        with client.apps.users.collections.documents.with_streaming_response.get(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.get(
                document_id="document_id",
                app_id="",
                user_id="user_id",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.get(
                document_id="document_id",
                app_id="app_id",
                user_id="",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.get(
                document_id="document_id",
                app_id="app_id",
                user_id="user_id",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.get(
                document_id="",
                app_id="app_id",
                user_id="user_id",
                collection_id="collection_id",
            )

    @parametrize
    def test_method_query(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.query(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            query="x",
        )
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Honcho) -> None:
        document = client.apps.users.collections.documents.query(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            query="x",
            filter={"foo": "bar"},
            top_k=1,
        )
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Honcho) -> None:
        response = client.apps.users.collections.documents.with_raw_response.query(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Honcho) -> None:
        with client.apps.users.collections.documents.with_streaming_response.query(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentQueryResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.query(
                collection_id="collection_id",
                app_id="",
                user_id="user_id",
                query="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.query(
                collection_id="collection_id",
                app_id="app_id",
                user_id="",
                query="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            client.apps.users.collections.documents.with_raw_response.query(
                collection_id="",
                app_id="app_id",
                user_id="user_id",
                query="x",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.create(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            content="x",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.create(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            content="x",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.documents.with_raw_response.create(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            content="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.documents.with_streaming_response.create(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            content="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.create(
                collection_id="collection_id",
                app_id="",
                user_id="user_id",
                content="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.create(
                collection_id="collection_id",
                app_id="app_id",
                user_id="",
                content="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.create(
                collection_id="",
                app_id="app_id",
                user_id="user_id",
                content="x",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.update(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.update(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
            content="x",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.documents.with_raw_response.update(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.documents.with_streaming_response.update(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.update(
                document_id="document_id",
                app_id="",
                user_id="user_id",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.update(
                document_id="document_id",
                app_id="app_id",
                user_id="",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.update(
                document_id="document_id",
                app_id="app_id",
                user_id="user_id",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.update(
                document_id="",
                app_id="app_id",
                user_id="user_id",
                collection_id="collection_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.list(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
        )
        assert_matches_type(AsyncPage[Document], document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.list(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            page=1,
            reverse=True,
            size=1,
            filter={"foo": "bar"},
        )
        assert_matches_type(AsyncPage[Document], document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.documents.with_raw_response.list(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(AsyncPage[Document], document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.documents.with_streaming_response.list(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(AsyncPage[Document], document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.list(
                collection_id="collection_id",
                app_id="",
                user_id="user_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.list(
                collection_id="collection_id",
                app_id="app_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.list(
                collection_id="",
                app_id="app_id",
                user_id="user_id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.delete(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )
        assert_matches_type(object, document, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.documents.with_raw_response.delete(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(object, document, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.documents.with_streaming_response.delete(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(object, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.delete(
                document_id="document_id",
                app_id="",
                user_id="user_id",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.delete(
                document_id="document_id",
                app_id="app_id",
                user_id="",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.delete(
                document_id="document_id",
                app_id="app_id",
                user_id="user_id",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.delete(
                document_id="",
                app_id="app_id",
                user_id="user_id",
                collection_id="collection_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.get(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.documents.with_raw_response.get(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(Document, document, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.documents.with_streaming_response.get(
            document_id="document_id",
            app_id="app_id",
            user_id="user_id",
            collection_id="collection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(Document, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.get(
                document_id="document_id",
                app_id="",
                user_id="user_id",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.get(
                document_id="document_id",
                app_id="app_id",
                user_id="",
                collection_id="collection_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.get(
                document_id="document_id",
                app_id="app_id",
                user_id="user_id",
                collection_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.get(
                document_id="",
                app_id="app_id",
                user_id="user_id",
                collection_id="collection_id",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.query(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            query="x",
        )
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncHoncho) -> None:
        document = await async_client.apps.users.collections.documents.query(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            query="x",
            filter={"foo": "bar"},
            top_k=1,
        )
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.users.collections.documents.with_raw_response.query(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.users.collections.documents.with_streaming_response.query(
            collection_id="collection_id",
            app_id="app_id",
            user_id="user_id",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentQueryResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.query(
                collection_id="collection_id",
                app_id="",
                user_id="user_id",
                query="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.query(
                collection_id="collection_id",
                app_id="app_id",
                user_id="",
                query="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_id` but received ''"):
            await async_client.apps.users.collections.documents.with_raw_response.query(
                collection_id="",
                app_id="app_id",
                user_id="user_id",
                query="x",
            )
