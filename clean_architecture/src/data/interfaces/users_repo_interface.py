from abc import ABC, abstractmethod

from src.domain.models.users import Users


class UsersRepoInterface(ABC):
    @abstractmethod
    def insert_user(
        self, first_name: str, last_name: str, age: int, email: str
    ) -> Users:
        raise NotImplementedError("get_user method must be implemented.")

    @abstractmethod
    def select_user(self, first_name: str) -> list[Users]:
        raise NotImplementedError("get_users method must be implemented.")

    # @abstractmethod
    # def create_user(self, user: User) -> User:
    #     raise NotImplementedError("create_usercreate_user method must be implemented.")

    # @abstractmethod
    # def update_user(self, user: User) -> User:
    #     raise NotImplementedError("update_user method must be implemented.")

    # @abstractmethod
    # def delete_user(self, user_id: int) -> User:
    #     raise NotImplementedError("delete_user method must be implemented.")
