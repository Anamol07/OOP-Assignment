# Defining a class Task to represent a single task
class Task:
    def __init__(self, title):
        # Initializinge task with a title and set it as not completed by default
        self.title = title
        self.completed = False 

    def mark_completed(self):
        # Marking this task as completed
        self.completed = True

    def change_title(self, new_title):
        # Changing the title of the task
        self.title = new_title

    def __str__(self):
        # Returning a formatted string showing the task status and title
        status = "Completed" if self.completed else " Not Completed"
        return f"[{status}] {self.title}"

# Defining a class TaskList to manage multiple tasks
class TaskList:
    def __init__(self, owner):
        # Storing the owner's name and initialize an empty task list
        self.owner = owner
        self.tasks = []

    def add_method(self, task):
        # Adding a new task to the list
        self.tasks.append(task)

    def remove_task(self, index):
        # Removing a task by its index if it's valid
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully.")
        else:
            print("Invalid task number.")

    def change_task_title(self, index, new_title):
        # Changing the title of a task at the given index
        if 0 <= index < len(self.tasks):
            self.tasks[index].change_title(new_title)
            print("Task renamed successfully.")
        else:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        # Marking the task at the given index as completed
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def view_task(self):
        # Displaying all tasks with their index and completion status
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print(f"\nTasks for {self.owner}:")
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")

    def list_options(self):
        # Providing a menu for the user to interact with the task list
        while True:
            print("\n--- To-Do List Manager ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Change task title")
            print("5. Mark task as completed")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Option to add a new task
                title = input("Enter a task: ")
                task = Task(title)
                self.add_method(task)

            elif choice == "2":
                # Option to view current tasks
                self.view_task()

            elif choice == "3":
                # Option to remove a task by index
                try:
                    a = int(input("Enter the index of the task to remove: "))
                    self.remove_task(a)
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "4":
                # Option to rename a task
                try:
                    b = int(input("Enter the index of the task to rename: "))
                    new_title = input("Enter the new title: ")
                    self.change_task_title(b, new_title)
                except ValueError:
                    print("Enter a valid number.")

            elif choice == "5":
                # Option to mark a task as completed
                try:
                    c = int(input("Enter the index of the task to mark as completed: "))
                    self.mark_task_completed(c)
                except ValueError:
                    print("Enter a valid number.")

            elif choice == "6":
                # Exiting the program
                print("Goodbye!")
                break

            else:
                # Handling invalid menu choices
                print("Invalid choice. Please try again.")

# Creating a TaskList object with predefined tasks
my_task_list = TaskList("Work")

# Adding some initial tasks to the list
my_task_list.tasks = [
    Task("Do Homework"),
    Task("Do Laundry"),
    Task("Go Shopping")
]

# Displaying the current tasks
my_task_list.view_task()

# Launching the task manager menu
my_task_list.list_options()