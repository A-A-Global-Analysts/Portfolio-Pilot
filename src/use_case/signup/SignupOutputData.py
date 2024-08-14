from abc import ABC, abstractmethod

class SignupOutputBoundary(ABC):
    @abstractmethod
    def prepare_success_view(self, user):
        pass

    @abstractmethod
    def prepare_fail_view(self, error: str):
        pass

    @abstractmethod
    def prepare_login_view(self):
        pass
