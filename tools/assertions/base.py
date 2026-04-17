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
