from faker import Faker


class Fake():
    """
   Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
   """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def password(self) -> str:
        """
        Генерирует случайный пароль.

        :return: Случайный пароль.
        """
        return self.faker.password()

    def user_name(self) -> str:
        """
        Генерирует случайный user_name.

        :return: Случайный user_name.
        """
        return self.faker.user_name()

    def display_name(self) -> str:
        """
        Генерирует случайный display_name.

        :return: Случайный display_name.
        """
        return self.faker.name()


# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())
