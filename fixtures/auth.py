import pytest

from clients.auth.auth_client import AuthClient, get_auth_client


@pytest.fixture
def auth_client() -> AuthClient:
    return get_auth_client()
