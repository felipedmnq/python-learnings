from src.domain.models.users import User
from src.infra.database.tests.users_repository_mock import UsersRepositorySpy

from pydantic import ValidationError

from .user_register import UserRegister


def test_register_user():
    users_repository = UsersRepositorySpy()
    user_register = UserRegister(users_repository)

    mock_user = User(first_name="John", last_name="Doe", age=30, email="test@test.com")
    response = user_register.register_user(mock_user)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["attributes"]["first_name"] == mock_user.first_name
    assert response["attributes"]["last_name"] == mock_user.last_name
    assert response["attributes"]["age"] == mock_user.age
    assert response["attributes"]["email"] == mock_user.email


def test_register_validation_error():
    users_repository = UsersRepositorySpy()
    user_register = UserRegister(users_repository)

    try:
        mock_user = User(first_name=123, last_name="Doe", age=30, email="test@test.com")
    except ValidationError as error:
        error_dict = error.errors()[0]
        assert error_dict["msg"] == "str type expected"
