from src.data.interfaces.users_repo_interface import UsersRepoInterface
from src.domain.use_cases.user_finder import UserFinderInterface
from src.infra.database.repositories.users_repository import UsersRepository


class UserFinder(UserFinderInterface):
    def __init__(self, users_repo: UsersRepoInterface) -> None:
        self.__users_repo = users_repo

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise TypeError("First name must contain only letters.")

    @classmethod
    def __format_response(cls, users: list) -> dict:
        return {
            "type": "Users",
            "count": len(users),
            "attributes": [user for user in users],
        }

    def __search_user(self, first_name: str) -> list:
        users = self.__users_repo.select_user(first_name)
        if users == []:
            raise KeyError(f"User with first name '{first_name}' not found.")

        return users

    def find_user(self, first_name: str) -> dict:
        self.__validate_name(first_name)
        users = self.__search_user(first_name)
        return self.__format_response(users)
