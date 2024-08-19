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


class AddStockPresenter:
    def present(self, output_data):
        print("Stock added successfully!")
        print(f"Stock Name: {output_data.get_stock_name()}")
        print(f"Symbol: {output_data.get_symbol()}")
        print(f"Date: {output_data.get_date()}")
        print(f"Value: {output_data.get_value()}")
        print(f"Volume: {output_data.get_volume()}")