from clients.auth.auth_schema import RegisterResponseSchema, TokenSchema
from tools.assertions.base import assert_equal, assert_is_true, assert_is_false, assert_is_zero


def assert_register_response(response: RegisterResponseSchema):
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response: Объект ответа с данными пользователями.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_is_true(response.id, "id")
    assert_is_true(response.email, "email")
    assert_is_true(response.username, "username")
    assert_is_true(response.display_name, "display_name")
    assert_is_true(response.bio, "bio")
    assert_is_true(response.avatar_url, "avatar_url")
    assert_is_true(response.cover_url, "cover_url")
    assert_is_true(response.role, "role")
    assert_is_true(response.is_active, "is_active")
    assert_is_false(response.is_verified, "is_verified")
    assert_is_false(response.is_private, "is_private")
    assert_is_true(response.created_at, "created_at")
    assert_is_true(response.updated_at, "updated_at")
    assert_is_zero(response.followers_count, "followers_count")
    assert_is_zero(response.following_count, "following_count")
    assert_is_zero(response.posts_count, "posts_count")
    assert_is_false(response.is_following, "is_following")
    assert_is_false(response.is_followed_by, "is_followed_by")


def assert_token_response(response: TokenSchema):
    """
    Проверяет корректность ответа при успешной авторизации.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если какое-либо из условий не выполняется.
    """
    assert_is_true(response.access_token, "access_token")
    assert_is_true(response.refresh_token, "refresh_token")
    assert_is_true(response.token_type, "token_type")