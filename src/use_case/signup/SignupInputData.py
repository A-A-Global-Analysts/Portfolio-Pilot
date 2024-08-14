class SignupInputData:

    def __init__(self, username, password, repeat_password):
        self._username = username
        self._password = password
        self._repeat_password = repeat_password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def repeat_password(self):
        return self._repeat_password