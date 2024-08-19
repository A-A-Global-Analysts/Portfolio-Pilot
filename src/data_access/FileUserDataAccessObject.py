import csv
import os
from datetime import datetime
from typing import Dict

class User:
    def __init__(self, username: str, password: str, creation_time: datetime, user_id: int):
        self.username = username
        self.password = password
        self.creation_time = creation_time
        self.user_id = user_id

    def get_name(self):
        return self.username

    def get_password(self):
        return self.password

    def get_creation_time(self):
        return self.creation_time

    def get_user_id(self):
        return self.user_id

class UserFactory:
    @staticmethod
    def create(username: str, password: str, creation_time: datetime, user_id: int) -> User:
        return User(username, password, creation_time, user_id)

class FileUserDataAccessObject:
    def __init__(self, csv_path: str, user_factory: UserFactory):
        self.csv_file = csv_path
        self.headers = {"username": 0, "password": 1, "creation_time": 2, "userID": 3}
        self.accounts: Dict[str, User] = {}
        self.user_factory = user_factory

        if os.path.getsize(self.csv_file) == 0:
            self._save()
        else:
            self._load()

    def _save(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers.keys())
            for user in self.accounts.values():
                writer.writerow([user.get_name(), user.get_password(), user.get_creation_time().isoformat(), user.get_user_id()])

    def _load(self):
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            for row in reader:
                username = row[self.headers["username"]]
                password = row[self.headers["password"]]
                creation_time_text = row[self.headers["creation_time"]]
                user_id = int(row[self.headers["userID"]])
                creation_time = datetime.fromisoformat(creation_time_text)
                user = self.user_factory.create(username, password, creation_time, user_id)
                self.accounts[username] = user

    def save_user(self, user: User):
        self.accounts[user.get_name()] = user
        self._save()

    def get_user_by_username(self, username: str) -> User:
        return self.accounts.get(username)

    def user_exists_by_name(self, identifier: str) -> bool:
        return identifier in self.accounts

    def delete_user(self, username: str):
        if username in self.accounts:
            del self.accounts[username]
            self._save()

    def get_user_id(self, username: str) -> int:
        return self.accounts[username].get_user_id() if username in self.accounts else None