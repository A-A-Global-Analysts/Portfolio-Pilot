import csv
import os
from datetime import datetime
from typing import List, Dict

class Investment:
    def __init__(self, ticker_symbol: str, purchase_date: datetime, quantity: float, value_at_purchase: float):
        self.ticker_symbol = ticker_symbol
        self.purchase_date = purchase_date
        self.quantity = quantity
        self.value_at_purchase = value_at_purchase

class Portfolio:
    def __init__(self, stocks: List[Investment], net_profit: float, user_id: int):
        self.stocks = stocks
        self.net_profit = net_profit
        self.user_id = user_id

class FilePortfolioDataAccessObject:
    STOCK_ATTRIBUTE_DELIMITER = "-"
    STOCK_ENTITY_DELIMITER = "_"

    def __init__(self, csv_path: str):
        self.csv_file = csv_path
        self.headers = {"userID": 0, "netProfit": 1, "stockList": 2}
        self.portfolios = {}

        if os.path.getsize(self.csv_file) == 0:
            self.save()
        else:
            self.load()

    def save(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers.keys())
            for portfolio in self.portfolios.values():
                encoded_stocks = self.encode_stock_list(portfolio.stocks)
                writer.writerow([portfolio.user_id, portfolio.net_profit, encoded_stocks])

    def load(self):
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                user_id = int(row[self.headers["userID"]])
                net_profit = float(row[self.headers["netProfit"]])
                encoded_stocks = row[self.headers["stockList"]]
                stocks = self.decode_stock_str(encoded_stocks)
                portfolio = Portfolio(stocks, net_profit, user_id)
                self.portfolios[user_id] = portfolio

    def decode_stock_str(self, encoded_stocks: str) -> List[Investment]:
        stocks = []
        for stock_str in encoded_stocks.split(self.STOCK_ENTITY_DELIMITER):
            ticker_symbol, value_at_purchase, quantity, purchase_date = stock_str.split(self.STOCK_ATTRIBUTE_DELIMITER)
            stocks.append(Investment(ticker_symbol, datetime.fromisoformat(purchase_date), float(quantity), float(value_at_purchase)))
        return stocks

    def encode_stock_list(self, stocks: List[Investment]) -> str:
        encoded_stocks = []
        for stock in stocks:
            encoded_stocks.append(f"{stock.ticker_symbol}{self.STOCK_ATTRIBUTE_DELIMITER}"
                                  f"{stock.value_at_purchase}{self.STOCK_ATTRIBUTE_DELIMITER}"
                                  f"{stock.quantity}{self.STOCK_ATTRIBUTE_DELIMITER}"
                                  f"{stock.purchase_date.isoformat()}")
        return self.STOCK_ENTITY_DELIMITER.join(encoded_stocks)

    def delete_portfolio(self, user_id: int):
        if user_id in self.portfolios:
            del self.portfolios[user_id]
            self.save()