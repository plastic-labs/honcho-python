# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho_core import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho_core._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Honcho) -> None:
        key = client.keys.create()
        assert_matches_type(object, key, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Honcho) -> None:
        key = client.keys.create(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            peer_id="peer_id",
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(object, key, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Honcho) -> None:
        response = client.keys.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(object, key, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Honcho) -> None:
        with client.keys.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(object, key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncHoncho) -> None:
        key = await async_client.keys.create()
        assert_matches_type(object, key, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHoncho) -> None:
        key = await async_client.keys.create(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            peer_id="peer_id",
            session_id="session_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(object, key, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHoncho) -> None:
        response = await async_client.keys.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(object, key, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHoncho) -> None:
        async with async_client.keys.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(object, key, path=["response"])

        assert cast(Any, response.is_closed) is True
