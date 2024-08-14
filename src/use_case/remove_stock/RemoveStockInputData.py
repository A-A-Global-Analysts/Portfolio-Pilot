class RemoveStockInputData:
    def __init__(self, ticker, username):
        self._ticker = ticker
        self._username = username

    @property
    def ticker(self):
        return self._ticker

    @property
    def username(self):
        return self._username