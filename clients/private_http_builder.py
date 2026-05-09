from httpx import Client
from pydantic import BaseModel

from clients.auth.public_auth_client import get_auth_client
from clients.auth.auth_schema import LoginRequestSchema
from config import settings


# class AuthenticationUserSchema(BaseModel, frozen=True):
#     email = str
#     password = str
#     # access_token: str
class AuthTokenSchema(BaseModel, frozen=True):
    access_token: str


def get_private_http_client(token: AuthTokenSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param token: Объект AuthTokenSchema с токеном пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # # Инициализируем AuthenticationClient для аутентификации
    # authentication_client = get_auth_client()
    #
    # # Инициализируем запрос на аутентификацию
    # login_request = LoginRequestSchema(email=user.email, password=user.password)
    # login_response = authentication_client.login(login_request)

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        # Добавляем заголовок авторизации
        headers={"Authorization": f"Bearer {token.access_token}"}
    )
