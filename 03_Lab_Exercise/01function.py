# Function to greet the user with optional university name (default is "UWS")
def greet_user(First_name, Last_name, University="UWS"):
    print(f"Hell0 {First_name} {Last_name} from {University}")

# Calling the greet_user function with a custom university name
greet_user("Anamoldip", "Rai", University="UWS Paisley")


# Function to add two numbers and return the result
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Calling add_numbers function and printing the result
result = add_numbers(1, 2)
print(result)

# Function that adds and multiplies two numbers, and returns both results
def add_numbers_and_Multiply(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product

# Storing the two returned values in separate variables
sum, product = add_numbers_and_Multiply(1, 2)

# Printing the results
print(sum)
print(product)