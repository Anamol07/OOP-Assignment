# Creating a list named colours with six colour names
colours = ["Black", "White", "Purple", "Pink", "Blue", "Yellow"]

# Printing the entire list
print(colours)  

# Accessing the second item (index 1) from the list and storing it in second_item
second_item = colours[1]

# Printing the second item
print(second_item)  

# Modifying the first element (index 0) of the list to "Brown"
colours[0] = "Brown"

# Printing the modified list
print(colours)  

# Getting the length of the list using len() function and storing it in length
length = len(colours)

# Printing the length of the list
print(length)  

# Checking if the string "red" is present in the list
if "red" in colours:
    print("Red is in the list")  
else:
    print("Red is not in the list")  

# Slicing the list to get elements from index 1 up to but not including index 3
selected_colours = colours[1:3]

# Printing the sliced list which contains two elements
print(selected_colours)  

