import pytest
from pydantic import BaseModel, EmailStr

from clients.auth.private_auth_client import PrivateAuthClient, get_private_auth_client
from clients.auth.public_auth_client import get_auth_client, PublicAuthClient
from clients.auth.auth_schema import RegisterRequestSchema, RegisterResponseSchema, LoginRequestSchema, TokenSchema
from clients.private_http_builder import AuthTokenSchema


class RegisterFixture(BaseModel):
    request: RegisterRequestSchema
    response: RegisterResponseSchema


class LoginFixture(BaseModel):
    request: LoginRequestSchema
    response: TokenSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def access_token(self) -> str:
        return self.response.access_token

    @property
    def refresh_token(self) -> str:
        return self.response.refresh_token

    @property
    def authentication_token(self) -> AuthTokenSchema:
        return AuthTokenSchema(
            access_token=self.access_token
        )


@pytest.fixture
def auth_client() -> PublicAuthClient:
    return get_auth_client()


@pytest.fixture
def private_auth_client(function_login_user: LoginFixture) -> PrivateAuthClient:
    return get_private_auth_client(function_login_user.authentication_token)


@pytest.fixture()
def function_register_user(auth_client: PublicAuthClient) -> RegisterFixture:
    request = RegisterRequestSchema()
    response = auth_client.register_api(request)
    print(response.text)
    response_model = RegisterResponseSchema.model_validate_json(response.text)

    return RegisterFixture(request=request, response=response_model)


@pytest.fixture()
def function_login_user(auth_client: PublicAuthClient, function_register_user: RegisterFixture) -> LoginFixture:
    request = LoginRequestSchema(
        email=function_register_user.response.email,
        password=function_register_user.request.password
    )
    response = auth_client.login_api(request)
    print(response.text)
    response_model = TokenSchema.model_validate_json(response.text)

    return LoginFixture(request=request, response=response_model)
