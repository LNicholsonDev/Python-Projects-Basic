# Assignment: Average MPG (Assignment 4)
# Class: DEV 108
# Date: 05/01/2024
# Author: Leah Nicholson
# Description: Program which computes fuel efficiency of a multi-leg journey for a vehicle.

# greeting

print()
print("Welcome to the Average MPG Calculator")
print()

# prompt for starting odometer

starting_odometer = 0
starting_odometer = int(input("Please enter the starting odometer reading in miles: "))

while (starting_odometer < 0):       # This is not starting_odometer >= 0:
    
    print()
    print("Starting odometer must be positive or zero - please try again.")
    print()
    starting_odometer = int(input("Please enter the starting odometer reading in miles: "))

# dividing line 
dashes = "-" * 100

# initialize variables - GOOD TILL THIS POINT
last_odometer_reading = 0
current_odometer_reading = starting_odometer
leg_number = 0
total_fuel = 0
more_input = 'y'

# while more_input is needed from user

while more_input.lower() == 'y':

    print(dashes)
    leg_number += 1

    last_odometer_reading = current_odometer_reading
    current_odometer_reading = float(input("Please enter new odometer reading in miles for leg #" + str(leg_number) + ": "))  # can only concatenate like type in input()
    fuel = float(input("Please enter fuel consumed in gallons for leg #" + str(leg_number) + ": "))
    
    total_fuel += fuel

    mpg = (current_odometer_reading - last_odometer_reading) / fuel
    
    print("MPG for leg # ", leg_number, ": ", mpg)
    print("Prior odometer reading: ", last_odometer_reading)
    print("Total fuel consumed: ", total_fuel)
    print("Fuel for current leg: ", fuel)
    print("Current odometer reading: ", current_odometer_reading)

    more_input = input("Continue? (y/n): ")

                     









# print leg_number
# calculate avg MPG over entire journey
# print avg MPG over entire journey and goodbye