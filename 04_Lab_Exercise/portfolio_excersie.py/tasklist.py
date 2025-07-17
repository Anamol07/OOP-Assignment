from tasks import Task
import datetime
from typing import List

class TaskList:
    """Manages a list of tasks."""

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a new task to the list."""
        self.tasks.append(task)

    def remove_task(self, index: int) -> None:
        """Removes task by index."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_task(self, index: int) -> Task:
        """Returns the task at the given index."""
        return self.tasks[index]

    def view_overdue_tasks(self) -> None:
        """Prints all tasks that are overdue based on current date."""
        now = datetime.datetime.now()
        overdue_tasks = [task for task in self.tasks if task.date_due < now and not task.completed]
        if not overdue_tasks:
            print("\nNo overdue tasks!\n")
            return
        print("\nOverdue Tasks:")
        for index, task in enumerate(overdue_tasks, start=1):
            print(f"\nTask {index}:")
            print(task)
            print("-" * 20)
