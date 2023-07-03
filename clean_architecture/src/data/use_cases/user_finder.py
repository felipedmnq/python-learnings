from src.data.interfaces.users_repo_interface import UsersRepoInterface
from src.domain.use_cases.user_finder import UserFinderInterface
from src.infra.database.repositories.users_repository import UsersRepository


class UserFinder(UserFinderInterface):
    def __init__(self, users_repo: UsersRepoInterface) -> None:
        self.__users_repo = users_repo

    def find_user(self, first_name: str) -> dict:
        if not first_name.isalpha():
            raise TypeError("First name must contain only letters.")

        users = self.__users_repo.select_user(first_name)

        if users == []:
            raise KeyError(f"User with first name '{first_name}' not found.")

        return {
            "type": "Users",
            "count": len(users),
            "attributes": [user.user for user in users],
        }
