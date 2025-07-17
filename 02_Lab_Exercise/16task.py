# Taking user input for temperature
temperature_input = float(input("Enter Temperature: "))

# Taking user input to determine the scale (Celsius, Kelvin, or Fahrenheit)
scale = input("Enter c for Celsius, k for Kelvin and f for Fahrenheit: ")

# If the user entered 'c', we assume the input is in Celsius
if scale == "c":
    degree_f = (temperature_input * 9/5) + 32   
    degree_k = temperature_input + 273.15      
    print(f"{temperature_input}°C is equal to {degree_f}°F and {degree_k}K")

# If the user entered 'k', we assume the input is in Kelvin
elif scale == "k":
    degree_C = temperature_input - 273.15       
    degree_f = (degree_C * 9/5) + 32            
    print(f"{temperature_input}K is equal to {degree_f}°F and {degree_C}°C")

# If the user entered 'f', we assume the input is in Fahrenheit
elif scale == "f":
    degree_C = (temperature_input - 32) * 5/9   
    degree_k = degree_C + 273.15              
    print(f"{temperature_input}°F is equal to {degree_k}K and {degree_C}°C")

# If the user enters something other than 'c', 'k', or 'f'
else:
    print("The inputted temperature scale is not valid")
   



