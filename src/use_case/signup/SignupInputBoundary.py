from abc import ABC, abstractmethod

class SignupInputBoundary(ABC):
    @abstractmethod
    def execute(self, signup_input_data):
        pass

    @abstractmethod
    def login(self):
        pass