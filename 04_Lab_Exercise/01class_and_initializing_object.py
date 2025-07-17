# Defining a class named Tasklist
class Tasklist:
    # Constructor that takes 'owner' as a parameter
    def __init__(self, owner):
        self.owner = owner           # Store the owner's name as-is (no formatting)
        self.tasks = []              # Initialize an empty list to hold tasks

# Creating an instance of Tasklist with owner "john"
my_task_list = Tasklist("john")
print(my_task_list.owner)           

# Creating another instance of Tasklist with owner "Jane"
someone_else_tasklist = Tasklist("Jane")
print(someone_else_tasklist.owner) 


# Defining a second class with a very similar name: TaskList 
class TaskList:
    # Constructor that takes 'owner' as a parameter
    def __init__(self, owner):
        self.owner = owner.upper()  # Convert the owner's name to uppercase
        self.tasks = []             # Initialize an empty list to hold tasks

# Creating an instance of TaskList with owner "Trioxide"
another_tasklist = TaskList("Trioxide")
print(another_tasklist.owner)     