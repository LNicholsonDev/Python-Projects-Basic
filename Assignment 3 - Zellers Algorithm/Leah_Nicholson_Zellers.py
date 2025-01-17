# Assignment: Zeller's Algorighm (Assignment 3)
# Class: DEV 108
# Date: 04/29/2024
# Author: Leah Nicholson
# Description: Program which displays the day of the week
#              for a given User-specified date between years 1582 - 4902.


# Ask for user inputs

print()
month = int(input("Enter month: "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))
print()

leap_status = False         # initialize leap_status tracker


# Validate year

if not (1582 <= year <= 4902):
    print("Invalid date input - year outside 1582 to 4902.")
    exit()


# Check if leap year per wiki definition
if year % 400 == 0:
    leap_status = True

elif year % 100 == 0:
    leap_status = False

elif year % 4 == 0:
    leap_status = True


# Validate month
if not (1 <= month <=12):
    print("Invalid date input - month outside 1 to 12.")
    exit()


# Validate day (For 31-day months, Feb (leap or non-leap), and 30-day months)

if (month == 1 or month == 3 or month == 5 \
    or month == 7 or month == 8 or month == 10 or month == 12):
    
    if not (1 <= day <= 31):
        print("Invalid date input - non feb month outside of 31 day bound.")
        exit()

elif (month == 2) and (leap_status == True):        # is a leap year (29 day)
       
    if not (1 <= day <= 29):
        print("Invalid date input - feb of leap year outside of 29 day bound.")
        exit()

elif (month == 2) and (leap_status == False):       # is not a leap year (28 day)

    if not (1 <= day <= 28):
        print("Invalid date input - feb of non leap year outside of 28 day bound.")
        exit()
    
else:

    if not (1 <= day <= 30):
        print("Invalid date input - non feb month outside of 30 day bound.")
        exit()


# Step 1: Adjust month and year

if (month == 1):
    month = 11
    year -= 1
elif (month == 2):
    month = 12
    year -= 1
elif (month == 3):
    month = 1
elif (month == 4):
    month = 2
elif (month == 5):
    month = 3
elif (month == 6):
    month = 4
elif (month == 7):
    month = 5
elif (month == 8):
    month = 6
elif (month == 9):
    month = 7
elif (month == 10):
    month = 8
elif (month == 11):
    month = 9
elif (month == 12):
    month = 10


# Step 2: Calculate intermediate values

a = month
b = day
c = year % 100
d = year // 100      # not (year - c) / 100

print("a b c d = ", a, b, c, int(d))


# Step 3: Compute final values

w = int((13 * a - 1) / 5)
x = int(c / 4)
y = int(d / 4)
z = int(w + x + y + b + c - 2 * d)
r = int(z % 7)

print("w x y z r =", w, x, y, z, r)


# Step 4: Adjust r and print out day of the week (r = day of week)

day_of_week = "None"    # Initialize weekday value

if r < 0:
    r += 7
    
if r == 0:
    day_of_week = "Sunday"

elif r == 1:
    day_of_week = "Monday"

elif r == 2:
    day_of_week = "Tuesday"

elif r == 3:
    day_of_week = "Wednesday"

elif r == 4:
    day_of_week = "Thursday"

elif r == 5:
    day_of_week = "Friday"

elif r == 6:
    day_of_week = "Saturday"


print("Day of the week: ", day_of_week)

