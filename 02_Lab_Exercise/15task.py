# Take input from the user and convert it to an integer
user_age = int(input("Enter your age: "))

# Check if the user is 18 or younger
if user_age <= 18:
    print("You are minor")  

# Check if the user is between 19 and 65 (inclusive)
elif user_age <= 65:
    print("You are an adult")  

# If the user is older than 65
else:
    print("You are a senior citizen")  