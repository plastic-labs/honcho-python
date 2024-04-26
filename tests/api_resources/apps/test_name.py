# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from honcho import Honcho, AsyncHoncho
from tests.utils import assert_matches_type
from honcho.types import App

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestName:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Honcho) -> None:
        name = client.apps.name.retrieve(
            "string",
        )
        assert_matches_type(App, name, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Honcho) -> None:
        response = client.apps.name.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = response.parse()
        assert_matches_type(App, name, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Honcho) -> None:
        with client.apps.name.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = response.parse()
            assert_matches_type(App, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Honcho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.apps.name.with_raw_response.retrieve(
                "",
            )


class TestAsyncName:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHoncho) -> None:
        name = await async_client.apps.name.retrieve(
            "string",
        )
        assert_matches_type(App, name, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHoncho) -> None:
        response = await async_client.apps.name.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        name = await response.parse()
        assert_matches_type(App, name, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHoncho) -> None:
        async with async_client.apps.name.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            name = await response.parse()
            assert_matches_type(App, name, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHoncho) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.apps.name.with_raw_response.retrieve(
                "",
            )
