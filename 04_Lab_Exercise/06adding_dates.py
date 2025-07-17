import datetime  # Importing the datetime module to work with dates and times

# Task class representing individual tasks
class Task:
    def __init__(self, title, date_due):
        # Initializing a Task object with a title, completion status, creation date, and due date
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now() 
        self.date_due = date_due  
    
    def mark_completed(self):
        # Marking the task as completed
        self.completed = True

    def change_title(self, new_title):
        # Changing the title of the task
        self.title = new_title

    def change_date_due(self, new_due):
        # Changing the due date of the task
        self.date_due = new_due  

    def __str__(self):
        # Returning a string representation of the task with status, title, creation, and due dates
        status = "Completed" if self.completed else "Not Completed"
        return (f"[{status}] {self.title} | "
                f"Created: {self.date_created.strftime('%Y-%m-%d')} | "
                f"Due: {self.date_due.strftime('%Y-%m-%d')}")


# TaskList class for managing a list of tasks
class TaskList:
    def __init__(self, owner):
        # Initializing the TaskList with an owner and an empty list of tasks
        self.owner = owner
        self.tasks = []

    def add_task(self, task):
        # Adding a Task object to the task list
        self.tasks.append(task)

    def remove_task(self, index):
        # Removing a task by its index if valid
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully.")
        else:
            print("Invalid task number.")

    def change_task_title(self, index, new_title):
        # Changing the title of a task at a specific index if valid
        if 0 <= index < len(self.tasks):
            self.tasks[index].change_title(new_title)
            print("Task renamed successfully.")
        else:
            print("Invalid task number.")

    def change_task_due_date(self, index, new_due):
        # Changing the due date of a task 
        if 0 <= index < len(self.tasks):
            self.tasks[index].change_date_due(new_due)
            print("Due date updated.")
        else:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        # Marking a task as completed 
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def view_task(self):
        # Displaying all tasks or a message if the task list is empty
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print(f"\nTasks for {self.owner}:")
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")

    def list_options(self):
        # Interactive menu for managing the task list
        while True:
            print("\n--- To-Do List Manager ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Change task title")
            print("5. Change task due date")
            print("6. Mark task as completed")
            print("7. Quit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                # Adding a new task 
                title = input("Enter a task: ")
                due_input = input("Enter due date (YYYY-MM-DD): ")
                try:
                    due_date = datetime.datetime.strptime(due_input, "%Y-%m-%d")
                    task = Task(title, due_date)
                    self.add_task(task)
                    print("Task added successfully.")
                except ValueError:
                    print(" Invalid date format. Use YYYY-MM-DD.")

            elif choice == "2":
                # Viewing the list of tasks
                self.view_task()

            elif choice == "3":
                # Removing a task
                try:
                    a = int(input("Enter the index of the task to remove: "))
                    self.remove_task(a)
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "4":
                # Changing the title of a task 
                try:
                    b = int(input("Enter the index of the task to rename: "))
                    new_title = input("Enter the new title: ")
                    self.change_task_title(b, new_title)
                except ValueError:
                    print("Enter a valid number.")

            elif choice == "5":
                # Changeing the due date of a task 
                try:
                    c = int(input("Enter the index of the task to change due date: "))
                    new_due = input("Enter the new due date (YYYY-MM-DD): ")
                    new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
                    self.change_task_due_date(c, new_due_date)
                except ValueError:
                    print("Invalid input. Make sure date is in YYYY-MM-DD format.")

            elif choice == "6":
                # Marking a task as completed 
                try:
                    d = int(input("Enter the index of the task to mark as completed: "))
                    self.mark_task_completed(d)
                except ValueError:
                    print("Enter a valid number.")

            elif choice == "7":
                # Exiting the program
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")




# Creating a TaskList instance with owner name "work"
my_task_list = TaskList("work")

# Prepopulating the task list with some tasks and due dates
my_task_list.tasks = [
    Task("Do Homework", datetime.datetime(2025, 7, 18)),
    Task("Do Laundry", datetime.datetime(2025, 7, 19)),
    Task("Go Shopping", datetime.datetime(2025, 7, 20))
]

# Displaying the initial tasks
my_task_list.view_task()

# Starting the interactive menu for managing tasks
my_task_list.list_options()
