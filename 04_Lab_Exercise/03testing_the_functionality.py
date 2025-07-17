# Defining the TaskList class to manage tasks for a given owner
class TaskList:
    # Constructor method to initialize the TaskList with an owner and an empty task list
    def __init__(self, owner):
        self.owner = owner.upper()  
        self.tasks = []             

    # Method to add a new task to the task list
    def add_task(self, task):
        self.tasks.append(task)    

    # Method to remove a task by its index
    def remove_task(self, index):
        # Checking if the index is valid before deleting
        if 0 <= index < len(self.tasks):
            del self.tasks[index]  
            print("Task removed successfully.")
        else:
            print("Invalid index. No task removed.")  

    # Method to display all tasks with their indices
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")  
        else:
            print(f"\nTasks for {self.owner}:")
            # Enumerate tasks to print index and task content
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")

    # Method to show an interactive menu and handle user actions
    def list_options(self):
        while True: 
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Quit")

            choice = input("Enter your choice: ")  

            if choice == "1":
                task = input("Enter a task: ")  
                self.add_task(task)              

            elif choice == "2":
                self.view_tasks()               

            elif choice == "3":
                try:
                    a = int(input("Enter the index of the task to remove: "))  
                    self.remove_task(a)       
                except ValueError:
                    print("Please enter a valid number.") 

            elif choice == "4":
                print("Goodbye!")  
                break            

            else:
                print("Invalid choice, please try again.")  


# Creating a TaskList instance with your name as the owner
my_task_list = TaskList("YOUR NAME")

# Adding some initial tasks for testing purposes
my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"]

# Starting the interactive menu
my_task_list.list_options()