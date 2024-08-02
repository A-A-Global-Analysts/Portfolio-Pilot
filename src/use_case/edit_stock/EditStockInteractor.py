from use_case.edit_stock import EditStockOutputData


class EditStockInteractor(EditStockInputBoundary):
    def __init__(self, logged_in_view_model, edit_stock_presenter, portfolio_data_access_interface, user_data_access_interface):
        self.logged_in_view_model = logged_in_view_model
        self.edit_stock_presenter = edit_stock_presenter
        self.portfolio_data_access_object = portfolio_data_access_interface
        self.user_data_access_object = user_data_access_interface
        

    def execute(self, edit_stock):
        try:
            ticker_symbol = edit_stock.get_ticker_symbol()
            new_quantity = edit_stock.get_new_quantity()

            username = edit_stock.get_username()
            user = self.user_data_access_object.get_user_from_username(username)
            user_id = user.get_user_id()
            portfolio = self.portfolio_data_access_object.get_portfolio_by_id(user_id)

            stock = portfolio.get_stock_by_ticker(ticker_symbol)
            stock.set_quantity(new_quantity)

            self.portfolio_data_access_object.save_portfolio(portfolio)

            tickers_to_quantities = portfolio.generate_tickers_to_quantities()

            output = EditStockOutputData(tickers_to_quantities)
            self.edit_stock_presenter.prepare_success_view(output)
        except Exception as e:
            self.edit_stock_presenter.prepare_fail_view(str(e))
            print(str(e))
