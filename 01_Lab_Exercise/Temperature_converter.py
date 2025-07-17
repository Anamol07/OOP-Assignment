# Taking user input for temperature in Celsius and converting it to a float
celsius_input = float(input("Enter Temperature in celsius: "))

# Converting Celsius to Fahrenheit
degree_f = (celsius_input * 9/5) + 32

# Converting Celsius to Kelvin
degree_k = celsius_input + 273.15

# Printing the temperature in Fahrenheit
print(f"{celsius_input} degree Celsius is equal to {degree_f} degree Fahrenheit")

# Printing the temperature in Kelvin
print(f"{celsius_input} degree Celsius is equal to {degree_k} degree Kelvin")