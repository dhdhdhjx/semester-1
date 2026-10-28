"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Layan
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
try:
    monthly = int(input("How much would you like to save every month? "))
except ValueError:
    print("Invalid amount")
    exit()


yearly = monthly * 12
print(f"You will save £{yearly} in a year.")

total = yearly * 1.008
print(f"Including interest, you will have £{total:.2f} after a year.")
