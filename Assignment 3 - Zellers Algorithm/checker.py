# Assignment: Zeller's Algorighm (Assignment 3)
# Class: DEV 108
# Date: 04/29/2024
# Author: Leah Nicholson
# Description: Program


# Ask for user inputs
print()

year = int(input("Enter the year: "))
print()


# Validate year
if not (1582 <= year <= 4902):
    print("Invalid date input.")
    exit()

# Check if leap
if year % 400 == 0:
    leap_status = True
    print("Leap status: True1")

elif year % 100 == 0:
    leap_status = False
    print("Leap status: False")

elif year % 4 == 0:
    leap_status = True
    print("Leap status: True2")



