import pytest
from pydantic import BaseModel
from clients.auth.auth_client import AuthClient, get_auth_client
from clients.auth.auth_schema import RegisterRequestSchema, RegisterResponseSchema


class AuthFixture(BaseModel):
    request: RegisterRequestSchema
    response: RegisterResponseSchema


@pytest.fixture
def auth_client() -> AuthClient:
    return get_auth_client()


@pytest.fixture()
def function_register_user(auth_client: AuthClient) -> AuthFixture:
    request = RegisterRequestSchema()
    response = auth_client.register_api(request)
    response_model = RegisterResponseSchema.model_validate_json(response.text)

    return AuthFixture(request=request, response=response_model)
