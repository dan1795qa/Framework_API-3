from httpx import Response
from clients.auth.auth_schema import LogoutRequestSchema
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthTokenSchema


class PrivateAuthClient(APIClient):
    """Клиент для работы с /api/auth/"""

    def logout_api(self, request: LogoutRequestSchema) -> Response:
        """
        Метод выполняет выход из системы.

        :param request: Словарь с refresh_token.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/auth/logout", json=request.model_dump(by_alias=True))


def get_private_auth_client(token: AuthTokenSchema) -> PrivateAuthClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return PrivateAuthClient(client=get_private_http_client(token))
