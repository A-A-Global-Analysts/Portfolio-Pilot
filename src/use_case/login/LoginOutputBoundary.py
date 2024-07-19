#Interface for the presenter
from abc import ABC, abstractmethod

class LoginOutputBoundary(ABC):
    @abstractmethod
    def prepare_success_view(self, user):
        pass

    @abstractmethod
    def prepare_fail_view(self, error: str):
        pass

    @abstractmethod
    def set_up_sign_up(self):
        pass