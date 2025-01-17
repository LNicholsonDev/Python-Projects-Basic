# Assignment: For Loops (Assignment 5)
# Class: DEV 108
# Date: 05/13/2024
# Author: Leah Nicholson
# Description: Program which creates patterns using for-loops given the user-specified size.

# welcome message
print()
print("Welcome to pattern generator")
print()

# prompt for user input
user_number = int(input("Please enter the size (an odd number between 7 and 15): "))

# validate input - odd number between 7 and 15 (inclusive)
while user_number not in range(7, 16, 2):
    print("Size should be an odd number between 7 and 15.")
    user_number = int(input("Please enter the size (an odd number between 7 and 15): "))

# first pattern
print()
print("Pattern 1 of size", user_number)
print()

for i in range(user_number, 0, -1):
    number_of_stars = (i + (i - 1))
    stars = "*" * number_of_stars
    parentheses = (user_number - number_of_stars) + i
    print("(" * parentheses, stars, ")" * parentheses, sep = "")

# second pattern 
print()
print("Mirror image pattern of size", user_number)
print()

total_characters = 2 * user_number

for i in range(1, user_number):
    space_count = total_characters - (2 * i)
    print(i * "A", space_count * " ", i * "A", sep = "")

for i in range(user_number, 0, -1):
    space_count = total_characters - (2 * i)
    print(i * "A", space_count * " ", i * "A", sep = "")

# exit message
print()
print("Bye")
