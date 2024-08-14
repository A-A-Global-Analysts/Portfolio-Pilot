class SignupOutputData:

    def __init__(self, username: str, creation_time: str, use_case_failed: bool):
        self._username = username
        self.creation_time = creation_time
        self.use_case_failed = use_case_failed

    @property
    def username(self) -> str:
        return self._username

    @property
    def creation_time(self) -> str:
        return self.creation_time

    @creation_time.setter
    def creation_time(self, creation_time: str):
        self.creation_time = creation_time