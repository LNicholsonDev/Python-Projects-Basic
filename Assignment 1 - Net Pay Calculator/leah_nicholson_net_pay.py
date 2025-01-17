# Assignment: Net Pay Calculator
# Class: DEV 108
# Date: 04/05/2024
# Author: Leah Nicholson
# Description: Program to calculate net pay - given hours worked, hourly rate, and tax withholding percent.


# Welcome statement
print("Welcome to Net Pay Calculator")
print()

# Inputs from user
name = input("Your name: ")
hours_worked = float(input("Hours Worked: "))
hourly_rate = float(input("Hourly Pay Rate: "))
tax_witholding = float(input("Tax witholding %: "))

# Calculations for gross pay, total with tax withheld, and net pay
gross_pay = hours_worked * hourly_rate
tax_withheld = gross_pay * (tax_witholding / 100)
net_pay = gross_pay - tax_withheld

# Convert values to strings for below print statement (concatenation of same type)
gross_pay = str(gross_pay)
net_pay = str(net_pay)

# Text Reporting to User
print()
print("Hello " + name + "!")
print("Your Gross Pay: " + "$" + gross_pay)
print("Your Net Pay: " + "$" + net_pay)
print("Good bye!")
