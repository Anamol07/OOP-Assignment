def compound_interest(principal, duration, interest_rate):
    # Check for valid interest rate
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    
    # Check for valid duration
    if duration < 0:
        print("Please enter a positive number of years")
        return None
    
    # Loop from year 1 to year 'duration' inclusive
    for year in range(1,duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year:.2f} £")
        
    return int(total_for_the_year)  # Return the final amount as an integer

# Call the function with example values
final_amount = compound_interest(10000, 6, 0.05)

# Print the final investment value
print(f"Final investment value: {final_amount} £")