from http import HTTPStatus
import time
from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import RegisterRequestSchema, RegisterResponseSchema, LoginRequestSchema, TokenSchema, \
    RefreshRequestSchema
from fixtures.auth import RegisterFixture, LoginFixture
from tools.assertions.auth import assert_register_response, assert_token_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


class TestAuth:

    def test_register(self, auth_client: AuthClient):
        request = RegisterRequestSchema()
        response = auth_client.register_api(request)
        response_model = RegisterResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_register_response(response_model)

        validate_json_schema(response.json(), response_model.model_json_schema())

    def test_login(self, auth_client: AuthClient, function_register_user: RegisterFixture):
        request = LoginRequestSchema(
            email=function_register_user.response.email,
            password=function_register_user.request.password
        )
        response = auth_client.login_api(request)
        response_model = TokenSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_token_response(response_model)

        validate_json_schema(response.json(), response_model.model_json_schema())


    def test_refresh(self, auth_client: AuthClient, function_login_user: LoginFixture):
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
