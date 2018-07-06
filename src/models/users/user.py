import uuid

from flask import session
import src.models.users.errors as Errors
from src.common.database import Database
from src.models.users import constants


class User(object):
    def __init__(self, email, password, _id=uuid.uuid4().hex):
        self.email = email
        self.password = password
        self._id = _id

    def json(self):
        return {
            "email": self.email,
            "password": self.password,
            "_id": self._id
        }

    def save_to_mongo(self):
        Database.insert(constants.collection, self.json())

    @staticmethod
    def login_is_valid(email, password):
        valid = Database.find_one(constants.collection, {"email": email})
        if valid is None:
            raise Errors.UserDoesntExist("User does not exist")
        elif valid['password']!=password :
            raise Errors.PasswordIncorrect("Password is Incorrect")
        else:
            return True

    @staticmethod
    def register_is_valid(email):
        """

        :param email:
        :return:
        """
        valid = Database.find_one(constants.collection, {"email": email})
        if valid is not None:
            raise Errors.UserAlreadyRegistered
        else:
            return True

    @classmethod
    def find_by_email(cls, email):
        return cls(**Database.find_one(constants.collection, {"email" : email}))

print(constants.collection)
