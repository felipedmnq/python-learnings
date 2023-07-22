from src.data.use_cases.user_finder import UserFinder
from src.infra.database.tests.users_repository_mock import UsersRepositorySpy


def test_find_user():
    first_name = "John"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)
    response = user_finder.find_user(first_name)

    assert repo.select_user_params["first_name"] == first_name
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"][0].first_name == first_name


def test_find_error_in_valid_name():
    first_name = "John_123"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find_user(first_name)
        assert False
    except Exception as error:
        assert str(error) == "First name must contain only letters."


def test_error_in_user_not_found():
    class UserFinderSpy(UsersRepositorySpy):
        def select_user(self, first_name: str) -> dict:
            return []

    first_name = "John"
    repo = UserFinderSpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find_user(first_name)
        assert False
    except Exception as error:
        assert (
            str(error).replace('"', "")
            == f"User with first name '{first_name}' not found."
        )
