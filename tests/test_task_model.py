# tests/test_task_model.py

import sys
import os

# Add the project root to the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.models.task import Task

def test_task_model():
    print(" Creating a new Task instance...")
    task = Task(
        task_id=1,
        user_id=1,
        title="Finish task model",
        description="Implement and test the Task class",
        due_date="2025-03-30",
        priority="High",
        status="Pending",
        tags=["oop", "model", "test"]
    )

    # Test getters
    print("\n Testing Getters:")
    print(" Task ID:", task.get_id())
    print(" User ID:", task.get_user_id())
    print(" Title:", task.get_title())
    print(" Description:", task.get_description())
    print(" Due Date:", task.get_due_date())
    print(" Priority:", task.get_priority())
    print(" Status:", task.get_status())
    print(" Tags:", task.get_tags())
    print(" Created At:", task.get_created_at())
    print(" Updated At:", task.get_updated_at())

    # Test setters
    print("\n Testing Setters:")
    task.set_title("Updated Task Title")
    task.set_status("In Progress")
    task.set_updated_at()

    print(" Updated Title:", task.get_title())
    print(" Updated Status:", task.get_status())
    print(" Updated Timestamp:", task.get_updated_at())

    # Convert to dictionary
    print("\n Serializing Task to Dictionary:")
    task_dict = task.to_dict()
    print(task_dict)

    # Reconstruct task from dictionary
    print("\n Reconstructing Task from Dictionary:")
    task2 = Task.from_dict(task_dict)
    print(" Reconstructed Task:", task2.to_dict())

if __name__ == "__main__":
    test_task_model()
