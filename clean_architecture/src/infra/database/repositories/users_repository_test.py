import pytest
from sqlalchemy import text
from src.domain.models.users import User
from src.infra.database.connection.db_connection import DBConnectionHandler

from pydantic import ValidationError

from .users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensitive test.")
def test_insert_user():
    """Should insert user into database"""

    mock_data = {
        "id_": 1001,
        "first_name": "first_name",
        "last_name": "last_name",
        "age": 99,
        "email": "test@test.com",
    }
    user = User(**mock_data)
    try:
        UsersRepository.insert_user(user)
    except ValidationError as error:
        print(f"\033[96m{error.json()}\033[0m")
    query = text(
        f"""
        SELECT * FROM users \
        WHERE first_name='{mock_data['first_name']}' \
        AND last_name='{mock_data['last_name']}' \
        AND age={mock_data['age']} \
        AND email='{mock_data['email']}';
    """
    )

    result = connection.execute(query)
    registry = result.fetchall()[0]

    assert registry.first_name == mock_data["first_name"]
    assert registry.last_name == mock_data["last_name"]
    assert registry.age == mock_data["age"]
    assert registry.email == mock_data["email"]

    connection.execute(text(f"DELETE FROM users WHERE id = {registry.id}"))


@pytest.mark.skip(reason="Sensitive test.")
def test_select_user():
    """Should select user from database"""

    mock_data = {
        "first_name": "first_name_2",
        "last_name": "last_name_2",
        "age": 1,
        "email": "test_2@test.com",
    }

    query = text(
        f"""
        INSERT INTO users (first_name, last_name, age, email) \
        VALUES ('{mock_data['first_name']}', '{mock_data['last_name']}', \
        {mock_data['age']}, '{mock_data['email']}');
    """
    )

    connection.execute(query)
    connection.commit()

    user = UsersRepository.select_user(mock_data["first_name"])[0]

    assert user.first_name == mock_data["first_name"]
    assert user.last_name == mock_data["last_name"]
    assert user.age == mock_data["age"]
    assert user.email == mock_data["email"]

    connection.execute(text(f"DELETE FROM users WHERE id = {user.id}"))
    connection.commit()
