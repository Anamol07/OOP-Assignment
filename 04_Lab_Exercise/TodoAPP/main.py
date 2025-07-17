from task_list import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Propagates a task list with some sample tasks."""
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))
    return task_list

def main():
    task_list = TaskList("YOUR NAME")  # Replace YOUR NAME with your actual name
    task_list = propagate_task_list(task_list)

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
            title = input("Enter a task: ")
            due_input = input("Enter due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.datetime.strptime(due_input, "%Y-%m-%d")
                task = Task(title, due_date)
                task_list.add_task(task)
                print("Task added successfully.")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

        elif choice == "2":
            task_list.view_task()

        elif choice == "3":
            try:
                ix = int(input("Enter the index of the task to remove: "))
                task_list.remove_task(ix)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                ix = int(input("Enter the index of the task to rename: "))
                new_title = input("Enter the new title: ")
                task_list.change_task_title(ix, new_title)
            except ValueError:
                print("Enter a valid number.")

        elif choice == "5":
            try:
                ix = int(input("Enter the index of the task to change due date: "))
                new_due = input("Enter the new due date (YYYY-MM-DD): ")
                new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
                task_list.change_task_due_date(ix, new_due_date)
            except ValueError:
                print("Invalid input. Make sure date is in YYYY-MM-DD format.")

        elif choice == "6":
            try:
                ix = int(input("Enter the index of the task to mark as completed: "))
                task_list.mark_task_completed(ix)
            except ValueError:
                print("Enter a valid number.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
