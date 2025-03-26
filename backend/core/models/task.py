# backend/core/models/task.py

from datetime import datetime

class Task:
    """
    Represents a Task entity with strict encapsulation using private attributes.
    """

    def __init__(self, task_id, user_id, title, description="", due_date=None,
                 priority="Low", status="Pending", tags=None,
                 created_at=None, updated_at=None):
        self.__id = task_id
        self.__user_id = user_id
        self.__title = title
        self.__description = description
        self.__due_date = due_date
        self.__priority = priority
        self.__status = status
        self.__tags = tags or []
        self.__created_at = created_at or datetime.now().isoformat()
        self.__updated_at = updated_at or self.__created_at

    # --------- Getters ---------

    def get_id(self):
        return self.__id

    def get_user_id(self):
        return self.__user_id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_due_date(self):
        return self.__due_date

    def get_priority(self):
        return self.__priority

    def get_status(self):
        return self.__status

    def get_tags(self):
        return self.__tags

    def get_created_at(self):
        return self.__created_at

    def get_updated_at(self):
        return self.__updated_at

    # --------- Setters ---------

    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_due_date(self, due_date):
        self.__due_date = due_date

    def set_priority(self, priority):
        self.__priority = priority

    def set_status(self, status):
        self.__status = status

    def set_tags(self, tags):
        self.__tags = tags

    def set_updated_at(self):
        self.__updated_at = datetime.now().isoformat()

    # --------- Serialization ---------

    def to_dict(self):
        """
        Convert the Task object to a dictionary for saving to JSON.
        """
        return {
            "id": self.__id,
            "user_id": self.__user_id,
            "title": self.__title,
            "description": self.__description,
            "due_date": self.__due_date,
            "priority": self.__priority,
            "status": self.__status,
            "tags": self.__tags,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Task object from a dictionary (loaded from file).
        """
        return cls(
            task_id=data.get("id"),
            user_id=data.get("user_id"),
            title=data.get("title"),
            description=data.get("description", ""),
            due_date=data.get("due_date"),
            priority=data.get("priority", "Low"),
            status=data.get("status", "Pending"),
            tags=data.get("tags", []),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at")
        )
