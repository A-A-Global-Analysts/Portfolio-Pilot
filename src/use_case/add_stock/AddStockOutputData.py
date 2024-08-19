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