# Assignment: Average MPG (Assignment 4)
# Class: DEV 108
# Date: 05/01/2024
# Author: Leah Nicholson
# Description: Program which computes fuel efficiency of a multi-leg journey for a vehicle.

# welcome message printed

print()
print("Welcome to the Average MPG Calculator")
print()

# user prompt for starting odometer

starting_odometer = 0
starting_odometer = float(input("Please enter the starting odometer reading in miles: "))
print()

# user prompt for starting odometer - input validated

while (starting_odometer < 0):       # This is not the same as starting_odometer >= 0:
    
    print()
    print("Starting odometer must be positive or zero - please try again.")
    print()
    starting_odometer = int(input("Please enter the starting odometer reading in miles: ")) # ask again for input if initially invalid

# dividing line 

dashes = "-" * 60

# initialize variables 

last_odometer_reading = 0
initial_start_odometer = starting_odometer
current_odometer_reading = starting_odometer
leg_number = 0
total_fuel = 0
more_input = 'y'

# while user indicates more input needed

while more_input.lower() == 'y':

    print(dashes)
    leg_number += 1
    last_odometer_reading = current_odometer_reading

    current_odometer_reading = float(input("Please enter new odometer reading in miles for leg #" + str(leg_number) + ": "))  # can only concatenate like type in input()
    fuel = float(input("Please enter fuel consumed in gallons for leg #" + str(leg_number) + ": "))
    
    if (fuel > 0) and (current_odometer_reading > last_odometer_reading):

        total_fuel += fuel
        mpg = (current_odometer_reading - last_odometer_reading) / fuel
        
        print("MPG for leg #", leg_number, "=", mpg)
        more_input = input("Continue (y/n)? ")

    else: 
        print("Fuel consumed needs to be positive and new odometer reading needs to be higher than", last_odometer_reading)
        current_odometer_reading = last_odometer_reading        # undo improper specification of odometer by user
        leg_number -= 1                                         # reduce leg count since it was an invalid leg

# calculate total distance and fuel consumed for final mpg

mpg_total = (current_odometer_reading - initial_start_odometer) / total_fuel

# print result (legs and final average)

print()
print("Total number of legs in the journey: ", leg_number)
print("Final average MPG for the entire journey: ", mpg_total)
print("Bye!")
