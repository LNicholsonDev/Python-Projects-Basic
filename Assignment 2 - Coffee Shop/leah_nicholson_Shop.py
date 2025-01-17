# Assignment: Shop Statement (Assignment 2)
# Class: DEV 108
# Date: 04/12/2024
# Author: Leah Nicholson
# Description: Program to generate a coffee shop statement, including date, cost, tax, and totals.

# formatting
dashline = "-" * 50              # * operator with a string and a number
star_dashline = "*" * 50         

# leading welcome
print(star_dashline)             # use variables for line separators
print("Welcome to LN Coffee Shop!")
print(star_dashline)

# initials

vertical_L = "\t | \t\t |"       
horizontal_L = "___________"

print(vertical_L + "\\" + "\t  |")  # Escape characters while printing
print(vertical_L + " \\" + "\t  |")
print(vertical_L + "  \\" + "\t  |")
print(vertical_L + "   \\" + "\t  |")
print(vertical_L + "    \\" + "\t  |")
print(vertical_L + "     \\" + "  |")
print(vertical_L + "      \\" + " |")
print("\t |" + horizontal_L + "\t |       \\" + "|")

print(star_dashline)

# get user input

print()
day_of_month = int(input("Please enter day of the month (1-31): "))
coffee_in_pounds = int(input("Please enter the amount of coffee in pounds: "))
print()

print(star_dashline)
print(dashline)

# calculations

coffee_charge = coffee_in_pounds * 7.50
shipping_charge = (0.85 * coffee_in_pounds) + 4.50
tax_rate = (31 - day_of_month) / 5
tax_charge = (coffee_charge * tax_rate) / 100
total = coffee_charge + shipping_charge + tax_charge

coffee_charge = round(coffee_charge, 2)
shipping_charge = round(shipping_charge, 2)
tax_charge = round(tax_charge, 2)
total = round(total, 2)

# display table with values

print("Shipping cost: ", shipping_charge)
print(dashline)

print("Date", "Cost", "Tax", "Total (Cost + Shipping + Tax)", sep="\t| ")  # Use of sep in print()
print(dashline)


print(day_of_month, coffee_charge, tax_charge, total, sep="\t| ")  # Today
print(dashline)

# recalculate Row 2 with new day_of_month
day_of_month += 1                           # Compound assignment operator +=
tax_rate = (31 - day_of_month) / 5          
tax_charge = (coffee_charge * tax_rate) / 100
total = coffee_charge + shipping_charge + tax_charge

coffee_charge = round(coffee_charge, 2)
shipping_charge = round(shipping_charge, 2)
tax_charge = round(tax_charge, 2)
total = round(total, 2)

print(day_of_month, coffee_charge, tax_charge, total, sep="\t| ")  # Tomorrow
print(dashline)

# recalculate Row 3 with new day_of_month
day_of_month += 1
tax_rate = (31 - day_of_month) / 5          
tax_charge = (coffee_charge * tax_rate) / 100
total = coffee_charge + shipping_charge + tax_charge

coffee_charge = round(coffee_charge, 2)
shipping_charge = round(shipping_charge, 2)
tax_charge = round(tax_charge, 2)
total = round(total, 2)

print(day_of_month, coffee_charge, tax_charge, total, sep="\t| ")  # Day-after
print(dashline)

print()
print("Bye, come again soon!")





























