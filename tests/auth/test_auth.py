from http import HTTPStatus

from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import RegisterRequestSchema, RegisterResponseSchema
from tools.assertions.auth import assert_register_response
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
