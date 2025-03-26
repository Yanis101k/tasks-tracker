# tests/test_auth_controller.py

import sys
import os

# Add the project root to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.controllers.auth_controller import AuthController

def test_auth_controller():
    print(" Testing AuthController (Register & Login)\n")

    # Step 1: Try registering a new user
    print(" Step 1: Registering a new user...")
    user = AuthController.register_user("yanis", "yanis@example.com", "1234")

    if user:
        print(" Registered successfully:", user.to_dict())
    else:
        print(" Could not register: User already exists.")

    # Step 2: Try registering the same user again
    print("\n Step 2: Attempting duplicate registration...")
    duplicate_user = AuthController.register_user("yanis", "yanis@example.com", "1234")

    if duplicate_user:
        print(" Error: Duplicate user was registered!")
    else:
        print(" Correct: Duplicate registration was blocked.")

    # Step 3: Try logging in with correct credentials
    print("\n Step 3: Logging in with correct credentials...")
    logged_in_user = AuthController.login_user("yanis@example.com", "1234")

    if logged_in_user:
        print(" Login successful:", logged_in_user.get_username())
    else:
        print(" Login failed with correct credentials.")

    # Step 4: Try logging in with wrong password
    print("\n Step 4: Logging in with incorrect password...")
    invalid_login = AuthController.login_user("yanis@example.com", "wrongpass")

    if invalid_login:
        print(" Error: Logged in with incorrect password!")
    else:
        print(" Correct: Login failed with incorrect password.")

if __name__ == "__main__":
    test_auth_controller()
