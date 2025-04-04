# tests/test_task_controller.py

import sys
import os

# Add the project root path so we can import backend modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.controllers.task_controller import TaskController

def test_task_controller():
    print(" Testing TaskController (Create, Read, Update, Delete)\n")

    # Step 1: Create a task for user_id 1
    print(" Creating a task...")
    task = TaskController.create_task(
        user_id=1,
        title="Test Task",
        description="This is a test task",
        due_date="2025-03-30",
        priority="High",
        status="Pending",
        tags=["urgent", "study"]
    )
    print(" Task created:", task.to_dict())

    # Step 2: Get all tasks for user_id 1
    print("\n Fetching tasks for user_id=1...")
    tasks = TaskController.get_tasks_by_user(1)
    print(f" Found {len(tasks)} task(s):")
    for t in tasks:
        print("-", t.to_dict()["title"])

    # Step 3: Update the task
    print("\n Updating task title and status...")
    success = TaskController.update_task(task.get_id(), {
        "title": "Updated Task Title",
        "status": "In Progress"
    })
    if success:
        print(" Task updated successfully.")
    else:
        print(" Failed to update task.")

    # Step 4: Try updating a non-existing task
    print("\n Attempting to update non-existing task (id=999)...")
    result = TaskController.update_task(999, {"title": "Should Fail"})
    print(" Correct behavior (should be False):", result)

    # Step 5: Delete the task
    print("\n Deleting the created task...")
    deleted = TaskController.delete_task(task.get_id())
    print(" Task deleted:", deleted)

    # Step 6: Try deleting again (should fail)
    print("\n Attempting to delete the same task again...")
    deleted_again = TaskController.delete_task(task.get_id())
    print(" Correct behavior (should be False):", deleted_again)
    
if __name__ == "__main__":
    test_task_controller()
