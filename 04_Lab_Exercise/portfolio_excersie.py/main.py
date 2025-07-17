from tasklist import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Propagates a task list with some sample tasks."""
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4), "Get vegetables and fruits"))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2), "Wash clothes"))
    task_list.add_task(Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1), "Organize desk and bed"))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3), "Math and Science"))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5), "Evening walk"))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6), "Kitchen cleanup"))
    return task_list

def main() -> None:
    task_list = TaskList("YOUR NAME")
    task_list = propagate_task_list(task_list)

    while True:
        print("\nOptions:")
        print("1: Add a new task")
        print("2: Remove a task")
        print("3: Mark a task as completed")
        print("4: Edit a task (title, due date, description)")
        print("5: View all tasks")
        print("6: View overdue tasks")
        print("7: Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            input_date = input("Enter due date (YYYY-MM-DD): ")
            description = input("Enter description (optional): ")
            try:
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object, description)
                task_list.add_task(task)
                print("Task added.")
            except ValueError:
                print("Invalid date format.")

        elif choice == "2":
            index = int(input("Enter task number to remove: ")) - 1
            task_list.remove_task(index)
            print("Task removed.")

        elif choice == "3":
            index = int(input("Enter task number to mark completed: ")) - 1
            task = task_list.get_task(index)
            task.mark_completed()
            print("Task marked as completed.")

        elif choice == "4":
            index = int(input("Enter task number to edit: ")) - 1
            task = task_list.get_task(index)
            new_title = input(f"Enter new title (leave empty to keep '{task.title}'): ")
            new_due = input(f"Enter new due date (YYYY-MM-DD) (leave empty to keep {task.date_due.strftime('%Y-%m-%d')}): ")
            new_desc = input(f"Enter new description (leave empty to keep current): ")

            if new_title:
                task.title = new_title
            if new_due:
                try:
                    task.date_due = datetime.datetime.strptime(new_due, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Keeping old date.")
            if new_desc:
                task.change_description(new_desc)
            print("Task updated.")

        elif choice == "5":
            print("\nAll Tasks:")
            for index, task in enumerate(task_list.tasks, start=1):
                print(f"\nTask {index}:")
                print(task)
                print("-" * 20)

        elif choice == "6":
            task_list.view_overdue_tasks()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
