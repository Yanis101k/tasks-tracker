import os
import json

class FileStorage:
    """
    Handles reading and writing data to JSON files (users and tasks).
    """

    # Base path of the project root (2 directories up from this file)
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

    # Full paths to JSON files
    USERS_FILE = os.path.join(BASE_DIR, 'data', 'users.json')
    TASKS_FILE = os.path.join(BASE_DIR, 'data', 'tasks.json')

    @staticmethod
    def ensure_data_files():
        """
        Ensure the data directory and files exist.
        If they exist but are empty, initialize them with an empty list.
        """
        data_dir = os.path.dirname(FileStorage.USERS_FILE)
        os.makedirs(data_dir, exist_ok=True)

        # Ensure users.json exists and is valid
        if not os.path.isfile(FileStorage.USERS_FILE) or os.path.getsize(FileStorage.USERS_FILE) == 0:
            with open(FileStorage.USERS_FILE, 'w') as f:
                json.dump([], f)

        # Ensure tasks.json exists and is valid
        if not os.path.isfile(FileStorage.TASKS_FILE) or os.path.getsize(FileStorage.TASKS_FILE) == 0:
            with open(FileStorage.TASKS_FILE, 'w') as f:
                json.dump([], f)

    @staticmethod
    def load_users():
        FileStorage.ensure_data_files()
        with open(FileStorage.USERS_FILE, 'r') as f:
            return json.load(f)

    @staticmethod
    def save_users(users):
        FileStorage.ensure_data_files()
        with open(FileStorage.USERS_FILE, 'w') as f:
            json.dump(users, f, indent=4)

    @staticmethod
    def load_tasks():
        FileStorage.ensure_data_files()
        with open(FileStorage.TASKS_FILE, 'r') as f:
            return json.load(f)

    @staticmethod
    def save_tasks(tasks):
        FileStorage.ensure_data_files()
        with open(FileStorage.TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
