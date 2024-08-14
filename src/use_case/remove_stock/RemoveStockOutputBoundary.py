from abc import ABC, abstractmethod

class RemoveStockOutputBoundary(ABC):
    @abstractmethod
    def prepare_success_view(self, output_data):
        pass

    @abstractmethod
    def prepare_fail_view(self, error: str):
        pass
