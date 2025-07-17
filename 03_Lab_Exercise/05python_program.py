tasks = []  # Initialize an empty list

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task added: '{task}'")

# Function to view current tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i} {task}")

# Function to remove a task from the list
def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task removed: '{removed}'")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    
    elif choice == "2":
        view_tasks()
    
    elif choice == "3":
        view_tasks()
        try:
            task_num = int(input("Enter the task number to remove: "))
            remove_task(task_num)
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "4":
        print("Exiting the To-Do List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")