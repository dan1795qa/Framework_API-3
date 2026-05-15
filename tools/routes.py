from enum import Enum


class APIRoutes(str, Enum):
    AUTH = "/api/auth"


    def __str__(self):
        return self.value
