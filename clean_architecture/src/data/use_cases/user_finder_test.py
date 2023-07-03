from src.data.use_cases.user_finder import UserFinder
from src.infra.database.tests.users_repository_mock import UsersRepositorySpy


def test_find_user():
    first_name = "John"

    repo = UsersRepositorySpy()
    # print(repo)
    user_finder = UserFinder(repo)
    response = user_finder.find_user(first_name)

    assert repo.select_user_params["first_name"] == first_name
    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"][0].first_name == first_name
