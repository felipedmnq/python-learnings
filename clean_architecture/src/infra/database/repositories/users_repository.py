from src.data.interfaces.users_repo_interface import UsersRepoInterface
from src.domain.models.users import User
from src.infra.database.connection.db_connection import DBConnectionHandler
from src.infra.database.entities.users import UserModel

from pydantic import ValidationError


class UsersRepository(UsersRepoInterface):
    @classmethod
    def insert_user(cls, user: User) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = UserModel(**user.__dict__)
                db_connection.session.add(new_user)
                db_connection.session.commit()

            except Exception as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def select_user(cls, first_name: str) -> list[UserModel]:
        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(UserModel)
                    .filter(UserModel.first_name == first_name)
                    .all()
                )
                return user

            except Exception as error:
                db_connection.session.rollback()
                raise error
