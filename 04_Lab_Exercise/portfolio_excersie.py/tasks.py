import datetime

class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime.datetime, description: str = "") -> None:
        """
        Creates a new task.

        Args:
            title (str): Title of the task.
            date_due (datetime.datetime): Due date of the task.
            description (str, optional): Description of the task. Defaults to "".
        """
        self.title = title
        self.date_due = date_due
        self.description = description
        self.completed = False

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def change_description(self, new_description: str) -> None:
        """Changes the description of the task.

        Args:
            new_description (str): The new description text.
        """
        self.description = new_description

    def __str__(self) -> str:
        """Returns a string representation of the task, including description."""
        status = "Completed" if self.completed else "Pending"
        return (f"Title: {self.title}\n"
                f"Due: {self.date_due.strftime('%Y-%m-%d')}\n"
                f"Description: {self.description}\n"
                f"Status: {status}")
