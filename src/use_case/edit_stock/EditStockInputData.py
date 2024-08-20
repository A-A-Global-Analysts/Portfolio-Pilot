class EditStockInputData:
    def __init__(self, ticker_symbol, new_quantity, username):
        self.ticker_symbol = ticker_symbol
        self.quantity = new_quantity
        self.username = username

    def get_ticker_symbol(self):
        return self.ticker_symbol

    def get_new_quantity(self):
        return self.quantity

    def get_username(self):
        return self.username

