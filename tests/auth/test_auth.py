from http import HTTPStatus
import time

from clients.auth.private_auth_client import PrivateAuthClient
from clients.auth.public_auth_client import PublicAuthClient
from clients.auth.auth_schema import RegisterRequestSchema, RegisterResponseSchema, LoginRequestSchema, TokenSchema, \
    RefreshRequestSchema, LogoutRequestSchema, GetMeResponseSchema
from fixtures.auth import RegisterFixture, LoginFixture
from tools.assertions.auth import assert_register_response, assert_token_response, assert_empty_response, \
    assert_get_me_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


class TestAuth:

    def test_register(self, auth_client: PublicAuthClient):
        request = RegisterRequestSchema()
        response = auth_client.register_api(request)
        print(response.text)
        response_model = RegisterResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_register_response(response_model)

        validate_json_schema(response.json(), response_model.model_json_schema())

    def test_login(self, auth_client: PublicAuthClient, function_register_user: RegisterFixture):
        request = LoginRequestSchema(
            email=function_register_user.response.email,
            password=function_register_user.request.password
        )
        response = auth_client.login_api(request)
        response_model = TokenSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_token_response(response_model)

        validate_json_schema(response.json(), response_model.model_json_schema())

    def test_refresh(self, auth_client: PublicAuthClient, function_login_user: LoginFixture):
        # time.sleep(0.8)
        request = RefreshRequestSchema(
            refresh_token=function_login_user.response.refresh_token
        )
        response = auth_client.refresh_api(request)
        print(response.text)
        response_model = TokenSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_token_response(response_model)

        validate_json_schema(response.json(), response_model.model_json_schema())

    def test_logout_user(self, private_auth_client: PrivateAuthClient, function_login_user: LoginFixture):
        request = LogoutRequestSchema(
            refresh_token=function_login_user.refresh_token
        )
        response = private_auth_client.logout_api(request)

        assert_status_code(response.status_code, HTTPStatus.NO_CONTENT)
        assert_empty_response(response)

    def test_get_me_user(self, private_auth_client: PrivateAuthClient):
        response = private_auth_client.get_me_api()
        print(response.text)
        response_model = GetMeResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_me_response(response_model)

        validate_json_schema(response.json(), response_model.model_json_schema())