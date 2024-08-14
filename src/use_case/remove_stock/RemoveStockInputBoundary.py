from abc import ABC, abstractmethod

class RemoveStockInputBoundary(ABC):
    @abstractmethod
    def execute(self, remove_stock_input_data):
        pass

