from src.data.interfaces.users_repo_interface import UsersRepoInterface
from src.domain.models.users import User as UserModel
from src.infra.database.connection.db_connection import DBConnectionHandler
from src.infra.database.entities.users import Users


class UsersRepository(UsersRepoInterface):
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int, email: str) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(UserModel(first_name, last_name, age, email))
                db_connection.session.add(new_user)
                db_connection.session.commit()

            except Exception as error:
                db_connection.session.rollback()
                raise error

    @classmethod
    def select_user(cls, first_name: str) -> list[Users]:
        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(Users)
                    .filter(Users.first_name == first_name)
                    .all()
                )
                return user

            except Exception as error:
                db_connection.session.rollback()
                raise error
