from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """

    assert actual == expected, (
        "Некорректный статус-код."
        f"Ожидается статус-код: {expected}."
        f"Актуальный стаутс-код: {actual}."
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """

    assert actual == expected, (
        f"Некорректное значение {name}."
        f"Ожидается статус-код: {expected}."
        f"Актуальный стаутс-код: {actual}."
    )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """

    assert actual or actual is None, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_is_false(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является ложным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение истинно.
    """
    assert not actual, (
        f'Incorrect value: "{name}". '
        f'Expected false value but got: {actual}'
    )


def assert_is_zero(actual: Any, name: str):
    """
    Проверяет, что фактическое значение равно нулю.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение не равно 0.
    """
    assert actual == 0, (
        f'Incorrect value: "{name}". '
        f'Expected 0 but got: {actual}'
    )
