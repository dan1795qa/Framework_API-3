from http import HTTPStatus

from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import RegisterRequestSchema
from tools.assertions.base import assert_status_code


class TestAuth:

    def test_register(self, auth_client: AuthClient):
        request = RegisterRequestSchema()
        response = auth_client.register_api(request)

        assert_status_code(response.status_code, HTTPStatus.CREATED)