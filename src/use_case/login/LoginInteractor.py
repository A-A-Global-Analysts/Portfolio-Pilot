#Takes input data and executes use case
from typing import Dict
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from use_case.login import LoginOutputBoundary

@dataclass
class Investment:
    ticker_symbol: str
    quantity: float

@dataclass
class Portfolio:
    net_profit: float
    stock_list: list[Investment]

@dataclass
class User:
    name: str
    user_id: int
    password: str

class LoginInputData:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class LoginOutputData:
    def __init__(self, name: str, user_id: int, is_signup: bool, net_profit: float, tickers_to_quantities: Dict[str, float]):
        self.name = name
        self.user_id = user_id
        self.is_signup = is_signup
        self.net_profit = net_profit
        self.tickers_to_quantities = tickers_to_quantities

class LoginUserDataAccessInterface:
    def exists_by_name(self, username: str) -> bool:
        pass

    def get_user_from_username(self, username: str) -> User:
        pass

class PortfolioDataAccessInterface:
    def get_portfolio_by_id(self, user_id: int) -> Portfolio:
        pass

class LoginInteractor:
    def __init__(self, user_data_access: LoginUserDataAccessInterface, login_presenter: LoginOutputBoundary, portfolio_data_access: PortfolioDataAccessInterface):
        self.user_data_access = user_data_access
        self.login_presenter = login_presenter
        self.portfolio_data_access = portfolio_data_access

    def signup(self):
        self.login_presenter.set_up_sign_up()

    def execute(self, login_input_data: LoginInputData):
        username = login_input_data.username
        password = login_input_data.password

        if not self.user_data_access.exists_by_name(username):
            self.login_presenter.prepare_fail_view(f"{username}: Account does not exist.")
        else:
            user = self.user_data_access.get_user_from_username(username)
            if password != user.password:
                self.login_presenter.prepare_fail_view(f"Incorrect password for {username}.")
            else:
                portfolio = self.portfolio_data_access.get_portfolio_by_id(user.user_id)
                overall_net_profit = portfolio.net_profit
                login_output_data = LoginOutputData(
                    user.name, user.user_id, False, self.round(overall_net_profit, 2),
                    self.generate_tickers_to_quantities(portfolio)
                )
                self.login_presenter.prepare_success_view(login_output_data)

    def round(self, value: float, places: int) -> float:
        if places < 0:
            raise ValueError("Number of places must be non-negative")

        return float(Decimal(value).quantize(Decimal(f"0.{'0'*places}"), rounding=ROUND_HALF_UP))

    def generate_tickers_to_quantities(self, portfolio: Portfolio) -> Dict[str, float]:
        tickers_to_quantities = {}
        for stock in portfolio.stock_list:
            tickers_to_quantities[stock.ticker_symbol] = tickers_to_quantities.get(stock.ticker_symbol, 0.0) + stock.quantity
        return {ticker: self.round(quantity, 2) for ticker, quantity in tickers_to_quantities.items()}
