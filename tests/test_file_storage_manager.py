import sys
import os

# Allow import from backend/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.file_storage_manager import FileStorage

def test_file_storage():
   
    print(" Loading existing users...")
    users = FileStorage.load_users()
    print(" Current users:", users)

    # Add a test user
    new_user = {
        "id": len(users) + 1,
        "username": "yanis_test",
        "email": "yanis@example.com",
        "password": "1234"
    }

    print("Adding a new user:", new_user)
    users.append(new_user)
    FileStorage.save_users(users)

    # Reload to verify
    updated_users = FileStorage.load_users()
    print(" Users after saving:", updated_users)

    print(" Loading existing tasks...")
    tasks = FileStorage.load_tasks()
    print(" Current tasks:", tasks)

    # Add a test task
    new_task = {
    "id": 1,
    "user_id": 1,
    "title": "Finish OOP assignment",
    "description": "Implement the User and Task models using file storage.",
    "due_date": "2025-03-30",  # Use string format: YYYY-MM-DD
    "priority": "High",        # Options: Low, Medium, High
    "status": "Pending",       # Options: Pending, In Progress, Completed
    "tags": ["school", "python", "oop"],
    "created_at": "2025-03-26T10:00:00",
    "updated_at": "2025-03-26T10:00:00"
}
   

    print("Adding a new task:", new_task)
    tasks.append(new_task)
    FileStorage.save_tasks(tasks)

    # Reload to verify
    updated_tasks = FileStorage.load_tasks()
    print(" Tasks after saving:", updated_tasks)

if __name__ == "__main__":
    test_file_storage()
