class LoggedInState:
    def __init__(self, user_state_manager, user):
        self.user_state_manager = user_state_manager
        self.user = user

    def login(self, user):
        print("User is already logged in.")

    def logout(self):
        print(f"Logging out user: {self.user.get_username()}")
        self.user_state_manager.set_user_state(LoggedOutState(self.user_state_manager))

    def get_current_user(self):
        return self.user


class LoggedOutState:
    def __init__(self, user_state_manager):
        self.user_state_manager = user_state_manager

    def login(self, user):
        print(f"Logging in user: {user.get_username()}")
        self.user_state_manager.set_user_state(LoggedInState(self.user_state_manager, user))

    def logout(self):
        print("No user is currently logged in.")

    def get_current_user(self):
        return None


class User:
    def __init__(self, username):
        self._username = username

    def get_username(self):
        return self._username


class UserStateManager:
    def __init__(self):
        self._current_state = LoggedOutState(self)

    def set_user_state(self, state):
        self._current_state = state

    def get_current_user(self):
        return self._current_state.get_current_user()