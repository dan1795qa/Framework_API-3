from pydantic import BaseModel, Field, ConfigDict
from typing import Any


class ValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ошибки валидации API.
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str = Field(alias='type')
    location: list[str | int] = Field(alias='loc')
    message: str = Field(alias='msg')
    input: Any
    context: dict[str, Any] = Field(alias='ctx')


class HTPPValidationErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ответа API с ошибкой валидации.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias='detail')


class UnauthorizedErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ответа API с ошибкой ауентификации.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias='detail')
    error_code: str = Field(alias='error_code')
    status_code: int = Field(alias='status_code')


class ForbiddenErrorSchema(BaseModel):
    """
    Модель, описывающая структуру ответа API с ошибкой авторизации.
    """
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias='detail')
