import pytest
from pydantic import BaseModel
from clients.auth.auth_client import AuthClient, get_auth_client
from clients.auth.auth_schema import RegisterRequestSchema, RegisterResponseSchema, LoginRequestSchema, TokenSchema


class RegisterFixture(BaseModel):
    request: RegisterRequestSchema
    response: RegisterResponseSchema


class LoginFixture(BaseModel):
    request: LoginRequestSchema
    response: TokenSchema


@pytest.fixture
def auth_client() -> AuthClient:
    return get_auth_client()


@pytest.fixture()
def function_register_user(auth_client: AuthClient) -> RegisterFixture:
    request = RegisterRequestSchema()
    response = auth_client.register_api(request)
    print(response.text)
    response_model = RegisterResponseSchema.model_validate_json(response.text)

    return RegisterFixture(request=request, response=response_model)


@pytest.fixture()
def function_login_user(auth_client: AuthClient, function_register_user: RegisterFixture) -> LoginFixture:
    request = LoginRequestSchema(
        email=function_register_user.response.email,
        password=function_register_user.request.password
    )
    response = auth_client.login_api(request)
    print(response.text)
    response_model = TokenSchema.model_validate_json(response.text)

    return LoginFixture(request=request, response=response_model)
