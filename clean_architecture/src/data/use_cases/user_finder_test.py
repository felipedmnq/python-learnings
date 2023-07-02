from src.data.use_cases.user_finder import UserFinder
from src.infra.database.repositories.users_repository import UsersRepository


def test_find_user():
    repo = UsersRepository()
    user_finder = UserFinder(repo)
    print(user_finder)
