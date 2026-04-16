from httpx import Response
from clients.auth.auth_schema import RegisterRequestSchema, LoginRequestSchema, TokenSchema
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class AuthClient(APIClient):
    """Клиент для работы с /api/auth/register"""

    def register_api(self, request: RegisterRequestSchema) -> Response:
        """
        Метод выполняет регистрацию пользователя пользователя.
        :param request: Словарь с email, user_name, password и display_name.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/auth/register", json=request.model_dump(by_alias=True))

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/auth/login", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> TokenSchema:
        response = self.login_api(request)
        # return response.json()
        return TokenSchema.model_validate_json(response.text)

# Добавляем builder для AuthClient
def get_auth_client() -> AuthClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthClient(client=get_public_http_client())
