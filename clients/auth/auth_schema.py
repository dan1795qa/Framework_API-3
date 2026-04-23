import uuid
from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from tools.fakers import fake


class TokenSchema(BaseModel):
    """Описание структуры аутентификационных токенов."""
    access_token: str
    refresh_token: str
    token_type: str


class RegisterRequestSchema(BaseModel):
    """Описание структуры запроса на регистрацию."""
    model_config = ConfigDict(populate_by_name=True)

    email: str = Field(default_factory=fake.email)
    user_name: str = Field(default_factory=fake.user_name, alias="username")
    password: str = Field(default_factory=fake.password)
    display_name: str = Field(default_factory=fake.display_name)


class RegisterResponseSchema(BaseModel):
    """Описание структуры ответа на регистрацию."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    username: str
    display_name: str
    bio: str | None
    avatar_url: str | None
    cover_url: str | None
    role: str
    is_active: bool
    is_verified: bool
    is_private: bool
    created_at: str
    updated_at: str
    followers_count: int
    following_count: int
    posts_count: int
    is_following: bool
    is_followed_by: bool


class LoginRequestSchema(BaseModel):
    """Описание структуры запроса на аутентификацию."""
    model_config = ConfigDict(populate_by_name=True)

    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class RefreshRequestSchema(BaseModel):
    """Описание структуры запроса на получение нового токена."""
    model_config = ConfigDict(populate_by_name=True)

    refresh_token: str

class LogooutRequestSchema(BaseModel):
    """Описание структуры запроса для разлогирования."""
    model_config = ConfigDict(populate_by_name=True)

    refresh_token: str


class GetMeResponseSchema(BaseModel):
    """Описание структуры ответа на регистрацию."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: str
    username: str
    display_name: str
    bio: str
    avatar_url: str
    cover_url: str
    role: str
    is_active: bool
    is_verified: bool
    is_private: bool
    created_at: str
    updated_at: str
    followers_count: int
    following_count: int
    posts_count: int
    is_following: bool
    is_followed_by: bool