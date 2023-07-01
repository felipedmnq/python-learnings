from abc import ABC, abstractmethod


class UserFinder(ABC):
    @abstractmethod
    def find_user(self) -> dict:
        raise NotImplementedError("find_user method not implemented.")
