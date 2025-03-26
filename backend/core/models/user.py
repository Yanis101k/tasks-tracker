# backend/core/models/user.py

from datetime import datetime

class User:
    """
    Represents a User entity with strictly private attributes.
    Follows strong encapsulation using __double_underscore naming.
    """

    def __init__(self, user_id, username, email, password, created_at=None):
        self.__id = user_id
        self.__username = username
        self.__email = email
        self.__password = password
        self.__created_at = created_at or datetime.now().isoformat()

    # --------- Getters ---------

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_created_at(self):
        return self.__created_at

    # --------- Setters ---------

    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    # --------- Serialization ---------

    def to_dict(self):
        """
        Convert the user object to a dictionary for saving to JSON.
        """
        return {
            "id": self.__id,
            "username": self.__username,
            "email": self.__email,
            "password": self.__password,
            "created_at": self.__created_at
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a User object from a dictionary loaded from JSON.
        """
        return cls(
            user_id=data.get("id"),
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
            created_at=data.get("created_at")
        )
