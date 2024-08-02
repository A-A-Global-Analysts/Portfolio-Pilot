from abc import ABC, abstractmethod

class EditStockUserDataAccessInterface(ABC):

    @abstractmethod
    def get_user_from_username(self, username):
        pass
