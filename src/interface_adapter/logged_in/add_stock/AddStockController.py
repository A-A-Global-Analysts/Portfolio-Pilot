class AddStockInputData:
    def __init__(self, stock_name, symbol, date, value, volume):
        self._stock_name = stock_name
        self._symbol = symbol
        self._date = date
        self._value = value
        self._volume = volume

    def get_stock_name(self):
        return self._stock_name

    def get_symbol(self):
        return self._symbol

    def get_date(self):
        return self._date

    def get_value(self):
        return self._value

    def get_volume(self):
        return self._volume


class AddStockInteractor:
    def __init__(self, add_stock_output_boundary, stock_gateway):
        self.add_stock_output_boundary = add_stock_output_boundary
        self.stock_gateway = stock_gateway

    def add_stock(self, input_data):
        self.stock_gateway.add_stock(input_data)
        output_data = AddStockOutputData(
            input_data.get_stock_name(),
            input_data.get_symbol(),
            input_data.get_date(),
            input_data.get_value(),
            input_data.get_volume()
        )
        self.add_stock_output_boundary.present_add_stock(output_data)


class AddStockController:
    def __init__(self, interactor):
        self.interactor = interactor

    def add_stock(self, stock_name, symbol, date, value, volume):
        input_data = AddStockInputData(stock_name, symbol, date, value, volume)
        self.interactor.add_stock(input_data)


# Example classes for the output boundary and stock gateway
class AddStockOutputData:
    def __init__(self, stock_name, symbol, date, value, volume):
        self._stock_name = stock_name
        self._symbol = symbol
        self._date = date
        self._value = value
        self._volume = volume

    def get_stock_name(self):
        return self._stock_name

    def get_symbol(self):
        return self._symbol

    def get_date(self):
        return self._date

    def get_value(self):
        return self._value

    def get_volume(self):
        return self._volume


class AddStockOutputBoundary:
    def present_add_stock(self, output_data):
        print(f"Stock Name: {output_data.get_stock_name()}")
        print(f"Symbol: {output_data.get_symbol()}")
        print(f"Date: {output_data.get_date()}")
        print(f"Value: {output_data.get_value()}")
        print(f"Volume: {output_data.get_volume()}")


class StockGateway:
    def add_stock(self, input_data):
        print(f"Adding stock: {input_data.get_stock_name()} with symbol {input_data.get_symbol()}")