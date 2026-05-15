from httpx import Response
from clients.auth.auth_schema import LogoutRequestSchema
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthTokenSchema
from tools.routes import APIRoutes


class PrivateAuthClient(APIClient):
    """Клиент для работы с /api/auth/"""

    def logout_api(self, request: LogoutRequestSchema) -> Response:
        """
        Метод выполняет выход из системы.

        :param request: Словарь с refresh_token.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"{APIRoutes.AUTH}/logout", json=request.model_dump(by_alias=True))


    def get_me_api(self) -> Response:
        """
        Метод выполняет выполняет запрос на получение информации о текущем авторизированном пользователе.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.AUTH}/me")

def get_private_auth_client(token: AuthTokenSchema) -> PrivateAuthClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AuthenticationClient.
    """
    return PrivateAuthClient(client=get_private_http_client(token))
