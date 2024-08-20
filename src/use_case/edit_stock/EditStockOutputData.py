class EditStockOutputData:
    def __init__(self, tickers_to_aggregated_quantities):
        self.tickers_to_aggregated_quantities = tickers_to_aggregated_quantities

    def get_tickers_to_aggregated_quantities(self):
        return self.tickers_to_aggregated_quantities
