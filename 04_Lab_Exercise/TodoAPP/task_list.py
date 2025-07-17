class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully.")
        else:
            print("Invalid task number.")

    def change_task_title(self, index, new_title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].change_title(new_title)
            print("Task renamed successfully.")
        else:
            print("Invalid task number.")

    def change_task_due_date(self, index, new_due):
        if 0 <= index < len(self.tasks):
            self.tasks[index].change_date_due(new_due)
            print("Due date updated.")
        else:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def view_task(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print(f"\nTasks for {self.owner}:")
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")