from src.data.interfaces.users_repo_interface import UsersRepoInterface
from src.domain.models.users import User
from src.domain.use_cases.user_registry import UserRegistryInterface


class UserRegister(UserRegistryInterface):
    def __init__(self, users_repo: UsersRepoInterface) -> None:
        self.__users_repo = users_repo

    def __register_user_info(self, user: User) -> None:
        self.__users_repo.insert_user(user)

    def __format_response(self, user: User) -> dict:
        return {
            "type": "User",
            "count": 1,
            "attributes": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
                "email": user.email,
            },
        }

    def register_user(self, user: User) -> dict:
        self.__register_user_info(user)
        return self.__format_response(user)
