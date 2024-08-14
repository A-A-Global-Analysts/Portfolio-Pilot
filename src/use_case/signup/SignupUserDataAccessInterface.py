from abc import ABC, abstractmethod
from entity import User

class SignupUserDataAccessInterface(ABC):
    @abstractmethod
    def exists_by_name(self, identifier: str) -> bool:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
