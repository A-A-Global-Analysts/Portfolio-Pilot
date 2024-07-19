#Stores login output data from user 
class LoginOutputData:
    def __init__(self, username, user_id, use_case_failed, net_profit, tickers_to_quantities):
        self.username = username
        self.user_id = user_id
        self.use_case_failed = use_case_failed
        self.net_profit = net_profit
        self.tickers_to_quantities = tickers_to_quantities

    def get_username(self):
        return self.username

    def get_user_id(self):
        return self.user_id

    def get_net_profit(self):
        return self.net_profit

    def set_net_profit(self, net_profit):
        self.net_profit = net_profit

    def get_tickers_to_quantities(self):
        return self.tickers_to_quantities

    def set_tickers_to_quantities(self, tickers_to_quantities):
        self.tickers_to_quantities = tickers_to_quantities