from src.data.interfaces.users_repo_interface import UsersRepoInterface
from src.domain.use_cases.user_finder import UserFinderInterface
from src.infra.database.repositories.users_repository import UsersRepository


class UserFinder(UserFinderInterface):
    def __init__(self, users_repo: UsersRepoInterface) -> None:
        self.__users_repo = users_repo

    def find_user(self, user_id: int) -> dict:
        user = self.user_repo.find_user(user_id)
        return user
