# Definining a global variable named 'my_new_variable' and assign it the value 0
my_new_variable = 0

# Definining a function named 'new_function'
def new_function():
    # Inside the function, a local variable named 'my_new_variable' is created
    # This local variable shadows the global one and is only accessible inside this function
    my_new_variable = 5
    
    # Printing the value of the local variable 
    print(my_new_variable)

# Calling the function 'new_function'
# This will print the local variable value, which is 5
new_function()

# Printing the value of the global variable
print(my_new_variable)
