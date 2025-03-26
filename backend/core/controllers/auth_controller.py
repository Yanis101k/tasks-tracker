# backend/core/controllers/auth_controller.py

from backend.core.file_storage_manager import FileStorage
from backend.core.models.user import User
import hashlib

class AuthController:
    """
    Controller class to handle user-related logic such as registration and login.
    Follows object-oriented and industry best practices.
    """

    @staticmethod
    def hash_password(password):
        """
        Hash a password using SHA-256.
        (In production, you'd use bcrypt with salt.)
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def find_user_by_email(email):
        """
        Look for a user with the given email in storage.
        Returns a User object or None.
        """
        users_data = FileStorage.load_users()
        for user_dict in users_data:
            if user_dict["email"] == email:
                return User.from_dict(user_dict)
        return None

    @staticmethod
    def find_user_by_username(username):
        """
        Look for a user with the given username in storage.
        Returns a User object or None.
        """
        users_data = FileStorage.load_users()
        for user_dict in users_data:
            if user_dict["username"] == username:
                return User.from_dict(user_dict)
        return None

    @staticmethod
    def register_user(username, email, password):
        """
        Register a new user if username and email are unique.
        Returns the created User object or None if already exists.
        """
        if AuthController.find_user_by_email(email) or AuthController.find_user_by_username(username):
            return None  # Duplicate user found

        users_data = FileStorage.load_users()

        new_user = User(
            user_id=len(users_data) + 1,
            username=username,
            email=email,
            password=AuthController.hash_password(password)
        )

        users_data.append(new_user.to_dict())
        FileStorage.save_users(users_data)

        return new_user

    @staticmethod
    def login_user(email, password):
        """
        Authenticate a user by checking email and password.
        Returns the User object if valid, or None if invalid.
        """
        user = AuthController.find_user_by_email(email)
        if user and user.get_password() == AuthController.hash_password(password):
            return user
        return None
