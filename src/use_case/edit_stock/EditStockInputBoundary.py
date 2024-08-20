from abc import ABC, abstractmethod

class EditStockInputBoundary(ABC):
    @abstractmethod
    def execute(self, input_data):
        pass
