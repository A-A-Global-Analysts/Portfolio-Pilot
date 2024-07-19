#User's database, check to make sure user exists

from entity import User

class LoginUserDataAccessInterface:
    def exists_by_name(self, identifier: str) -> bool:
        pass

    def save(self, user: User) -> None:
        pass

    def get_user_from_username(self, username: str) -> User:
        pass