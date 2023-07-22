from abc import ABC, abstractmethod

from src.domain.models.users import User


class UsersRepoInterface(ABC):
    @abstractmethod
    def insert_user(self, user: User) -> None:
        raise NotImplementedError("get_user method must be implemented.")

    @abstractmethod
    def select_user(self, first_name: str) -> list[User]:
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
