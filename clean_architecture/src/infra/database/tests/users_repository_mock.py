from src.domain.models.users import User
from src.domain.models.users import User as UserModel
from src.domain.models.users import Users


class UsersRepositorySpy:
    def __init__(self) -> None:
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(
        self, first_name: str, last_name: str, age: int, email: str
    ) -> None:
        self.insert_user_params["first_name"] = first_name
        self.insert_user_params["last_name"] = last_name
        self.insert_user_params["age"] = age
        self.insert_user_params["email"] = email

        return None

    def select_user(self, first_name: str) -> list[Users]:
        self.select_user_params["first_name"] = first_name

        response = [
            Users(
                User(
                    id=15,
                    first_name="John",
                    last_name="Doe",
                    age=30,
                    email="jd@mock.com",
                )
            ),
            Users(
                User(
                    id=14,
                    first_name="Johnny",
                    last_name="Doeny",
                    age=30,
                    email="jdny@mock.com",
                )
            ),
            Users(
                User(
                    id=13, first_name="Joh", last_name="Do", age=30, email="j@mock.com"
                )
            ),
        ]

        return response
