# Defining a function named calculate_tax that takes two arguments:
def calculate_tax(income, tax_rate):
    tax_amount = income * tax_rate  # Calculate the tax by multiplying income and tax rate
    return tax_amount  # Return the computed tax amount

# Calling the function with an income of 60000 and a tax rate of 0.3 (30%)
tax_amoount = calculate_tax(60000, 0.3)

# Printing the result
print(tax_amoount)

