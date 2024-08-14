from typing import List, Dict
from entity import Investment, Portfolio, User
from use_case import PortfolioDataAccessInterface
from use_case.remove_stock import RemoveStockOutputData

class RemoveStockInteractor:
    def __init__(self, user_data_access_object, portfolio_data_access_object, remove_stock_presenter):
        self.user_data_access_object = user_data_access_object
        self.portfolio_data_access_object = portfolio_data_access_object
        self.remove_stock_presenter = remove_stock_presenter

    def execute(self, remove_stock_input_data):
        try:
            ticker_symbol = remove_stock_input_data.get_ticker()  # Ticker of Stock that needs to be removed
            username = remove_stock_input_data.get_username()
            user = self.user_data_access_object.get_user_from_username(username)
            user_id = user.get_user_id()
            portfolio = self.portfolio_data_access_object.get_portfolio_by_id(user_id)  # Current user's portfolio
            stock_list = portfolio.get_stock_list()

            stock = portfolio.get_stock_by_ticker(ticker_symbol)  # Stock to be removed
            stock_list.remove(stock)  # Removes the stock

            portfolio.set_stock_list(stock_list)  # Updates the stock list

            tickers_to_quantities = portfolio.generate_tickers_to_quantities()

            self.portfolio_data_access_object.save_portfolio(portfolio)  # Saves user's portfolio to the database

            output_data = RemoveStockOutputData(tickers_to_quantities)
            self.remove_stock_presenter.prepare_success_view(output_data)
        except Exception as e:
            self.remove_stock_presenter.prepare_fail_view(str(e))
            print(str(e))
