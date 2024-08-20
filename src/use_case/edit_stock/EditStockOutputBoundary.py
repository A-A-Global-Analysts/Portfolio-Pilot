from abc import ABC, abstractmethod

class EditStockOutputBoundary(ABC):

    @abstractmethod
    def prepare_success_view(self, output):
        pass

    @abstractmethod
    def prepare_fail_view(self, error):
        pass
