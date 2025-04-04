# tests/test_user_model.py

import sys
import os

# Add the project root to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.models.user import User

def test_user_model():
    print(" Creating a new User instance...")
    user = User(1, "yanis", "yanis@example.com", "1234")

    # Test getters
    print("\n Testing Getters:")
    print(" ID:", user.get_id())
    print(" Username:", user.get_username())
    print(" Email:", user.get_email())
    print(" Password:", user.get_password())
    print(" Created At:", user.get_created_at())

    # Test setters
    print("\n Testing Setters:")
    user.set_username("yanis_updated")
    user.set_email("updated@example.com")
    user.set_password("new_password")

    print(" Updated Username:", user.get_username())
    print(" Updated Email:", user.get_email())
    print(" Updated Password:", user.get_password())

    # Convert to dictionary
    print("\n Serializing User to Dictionary:")
    user_dict = user.to_dict()
    print(user_dict)

    # Reconstruct user from dictionary
    print("\n Reconstructing User from Dictionary:")
    user2 = User.from_dict(user_dict)
    print(" Reconstructed User:", user2.to_dict())

if __name__ == "__main__":
    test_user_model()