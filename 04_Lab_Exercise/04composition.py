# Defining a class Task to represent a single task
class Task:
    def __init__(self, title):
        # Initialize the task with a title
        self.title = title

    def __str__(self):
        # Return a string representation of the task when printed
        return f"Task: {self.title}"


# Defining a class TaskList to manage multiple tasks
class TaskList:
    def __init__(self, owner):
        # Initializing the task list with an owner name and an empty list of tasks
        self.owner = owner
        self.tasks = []

    def add_method(self, task):
        # Adding a Task object to the tasks list
        self.tasks.append(task)

    def remove_task(self, index):
        # Removing a task by index if it's valid
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully")
        else:
            print("Invalid task number")

    def view_task(self):
        # Showing all tasks in the list
        if not self.tasks:
            print("No task in the list")
        else:
            print(f"Tasks for {self.owner}:")
            for i, task in enumerate(self.tasks):
                # Printing each task with its index
                print(f"{i}: {task}")

    def list_options(self):
        # Providing a menu for the user to interact with the task list
        while True:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Adding a new task
                title = input("Enter a task: ")
                task = Task(title)  # Create a Task object
                self.add_method(task)  # Add it to the task list

            elif choice == "2":
                # Viewing all tasks
                self.view_task()

            elif choice == "3":
                # Removing a task
                try:
                    a = int(input("Enter the index of the task to remove: "))
                    self.remove_task(a)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                # Exiting the loop and program
                print("Goodbye!")
                break

            else:
                print("Invalid choice, please try again.")


# Creating a TaskList object with predefined tasks
my_task_list = TaskList("Work")
my_task_list.tasks = [
    Task("Do Homework"),
    Task("Do Laundry"),
    Task("Go Shopping")
]

# Showing the current tasks
my_task_list.view_task()

# Starting the task manager menu
my_task_list.list_options()