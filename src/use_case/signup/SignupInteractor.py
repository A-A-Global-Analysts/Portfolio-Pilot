from datetime import datetime
from entity import Portfolio, User, UserFactory
from use_case import PortfolioDataAccessInterface
from use_case.signup import SignupOutputData

class SignupInteractor:
    def __init__(self, signup_data_access_interface, portfolio_data_access_object, signup_output_boundary, user_factory):
        self.user_data_access_object = signup_data_access_interface
        self.portfolio_data_access_object = portfolio_data_access_object
        self.user_presenter = signup_output_boundary
        self.user_factory = user_factory

    def login(self):
        self.user_presenter.prepare_login_view()

    def execute(self, signup_input_data):
        if self.user_data_access_object.exists_by_name(signup_input_data.get_username()):
            self.user_presenter.prepare_fail_view("User already exists.")
        elif signup_input_data.get_password() != signup_input_data.get_repeat_password():
            self.user_presenter.prepare_fail_view("Passwords don't match.")
        else:
            now = datetime.now()
            user = self.user_factory.create(signup_input_data.get_username(), signup_input_data.get_password(), now, hash(now))
            self.user_data_access_object.save(user)

            initial_portfolio = Portfolio([], 0, user.get_user_id())
            self.portfolio_data_access_object.save_portfolio(initial_portfolio)

            signup_output_data = SignupOutputData(user.get_name(), now.isoformat(), False)
            self.user_presenter.prepare_success_view(signup_output_data)