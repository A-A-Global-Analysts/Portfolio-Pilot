#Interface for LoginInteractor
# what is a fork on GitHub?
from abc import ABC, abstractmethod
from use_case.login import LoginInputData
class LoginInputBoundary(ABC):
    @abstractmethod
    def execute(self, login_input_data: LoginInputData) -> None:
        pass

    @abstractmethod
    def signup(self) -> None:
        pass
