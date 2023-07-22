from abc import ABC, abstractmethod

from src.domain.models.users import User


class UserRegistryInterface(ABC):
    @abstractmethod
    def register_user(self, user: User) -> dict:
        raise NotImplementedError("register_user method not implemented.")
