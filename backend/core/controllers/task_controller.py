# backend/core/controllers/task_controller.py

from backend.core.file_storage_manager import FileStorage
from backend.core.models.task import Task
from datetime import datetime

class TaskController:
    """
    Controller class to manage Task operations such as:
    - Creating tasks
    - Updating tasks
    - Deleting tasks
    - Retrieving tasks
    """

    @staticmethod
    def load_all_tasks():
        """
        Load all tasks from the file and return them as Task objects.
        """
        tasks_data = FileStorage.load_tasks()
        return [Task.from_dict(task) for task in tasks_data]

    @staticmethod
    def save_all_tasks(task_objects):
        """
        Save a list of Task objects back to the JSON file.
        """
        task_dicts = [task.to_dict() for task in task_objects]
        FileStorage.save_tasks(task_dicts)

    @staticmethod
    def create_task(user_id, title, description="", due_date=None,
                    priority="Low", status="Pending", tags=None):
        """
        Create a new task for the given user and save it.
        Returns the created Task object.
        """
        tasks = TaskController.load_all_tasks()
        new_task = Task(
            task_id=len(tasks) + 1,
            user_id=user_id,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=status,
            tags=tags or [],
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        tasks.append(new_task)
        TaskController.save_all_tasks(tasks)
        return new_task

    @staticmethod
    def get_tasks_by_user(user_id):
        """
        Return a list of Task objects that belong to the given user ID.
        """
        tasks = TaskController.load_all_tasks()
        return [task for task in tasks if task.get_user_id() == user_id]

    @staticmethod
    def update_task(task_id, updates: dict):
        """
        Update a task by its ID with fields provided in the updates dictionary.
        Returns True if updated successfully, False if not found.
        """
        tasks = TaskController.load_all_tasks()
        updated = False

        for task in tasks:
            if task.get_id() == task_id:
                if "title" in updates:
                    task.set_title(updates["title"])
                if "description" in updates:
                    task.set_description(updates["description"])
                if "due_date" in updates:
                    task.set_due_date(updates["due_date"])
                if "priority" in updates:
                    task.set_priority(updates["priority"])
                if "status" in updates:
                    task.set_status(updates["status"])
                if "tags" in updates:
                    task.set_tags(updates["tags"])

                task.set_updated_at()
                updated = True
                break

        if updated:
            TaskController.save_all_tasks(tasks)
        return updated

    @staticmethod
    def delete_task(task_id):
        """
        Delete a task by its ID.
        Returns True if deleted, False if task was not found.
        """
        tasks = TaskController.load_all_tasks()
        filtered_tasks = [task for task in tasks if task.get_id() != task_id]

        if len(filtered_tasks) != len(tasks):
            TaskController.save_all_tasks(filtered_tasks)
            return True
        return False
