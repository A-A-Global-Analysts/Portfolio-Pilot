from src.use_case.delete_user.DeleteInputBoundary import DeleteInputBoundary
from src.use_case.delete_user.DeleteOutputBoundary import DeleteOutputBoundary
from src.use_case.delete_user.DeleteUserDataAccessInterface import DeleteUserDataAccessInterface
from src.use_case.delete_user.DeletePortfolioAccessInterface import DeletePortfolioAccessInterface
from src.use_case.delete_user.DeleteOutputData import DeleteOutputData

class DeleteInteractor(DeleteInputBoundary):
    def __init__(self, delete_data_access_object: DeleteUserDataAccessInterface, delete_presenter: DeleteOutputBoundary, portfolio_data_access_object: DeletePortfolioAccessInterface):
        self.delete_presenter = delete_presenter
        self.delete_data_access_object = delete_data_access_object
        self.delete_portfolio_data_access_object = portfolio_data_access_object

    def execute(self, username: str):
        try:
            user_id = self.delete_data_access_object.get_user_id(username)
            self.delete_data_access_object.delete_user(username)
            self.delete_portfolio_data_access_object.delete_portfolio(user_id)
            output = DeleteOutputData(username, True)
            self.delete_presenter.prepare_success_view(output)
        except Exception as e:
            self.delete_presenter.prepare_fail_view(str(e))
            print(e)
