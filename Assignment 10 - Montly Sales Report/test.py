# Assignment: Monthly Sales Report (Assignment 10)
# Class: DEV 108
# Date: 06-14-2024
# Author: Leah Nicholson
# Description: Program which allows a User to calculate total yearly sales and average montly sales from a .csv file source.
# User may update the value for any given month - data changes are persistent.

#!/usr/bin/env python3

import csv
import sys

# a file in the current directory
FILENAME = "monthly_sales.csv"

# helper list
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def read_sales():
    ''' Function to read contents of .csv FILENAME and return the contents as list of lists. '''

    with open(FILENAME, newline = "") as file:

        data_list = []                  # needed to capture and store the data, and return it
        contents = csv.reader(file)

        for row in contents:
            row[1] = int(row[1])        # convert each of the second items (the dates) to integers
            data_list.append(row)       # append the whole row of data to the new list (for each row in contents)
        
    return data_list                    # actually return the data so it can be used


def write_sales(sales):
    ''' Function to write the contents of sales, a list of lists, to FILENAME. '''

    with open(FILENAME, "w", newline = "") as file:

        writer = csv.writer(file)
        writer.writerows(sales) 


def view_monthly_sales(sales):
    ''' Function to print the monthly sales values. '''

    print()

    for item in sales:
        print(item[0], " - ", item[1])
    
    print()


def edit(sales):
    ''' Let user edit the sales value for one of the months.
    - Prompt the user for 3-letter month code. Raise an exception if user enters an
        invalid code. 
    - Prompt the user for the new sales numbers.
    - Use a try/except block that will handle invalid input in both the cases.
    '''

    try:

        month = input("Three-letter month: ")
        month = month.lower()                   # makes the user input title case to check the MONTH_NAMES list

        if month.title() not in MONTH_NAMES:
            raise ValueError

    except ValueError:
        print("ValueError: Invalid three-letter month.")




    for item in sales:
                
        if item[0].lower() == month:        # makes the item in the list lowercase
                    
            montly_sales_data = item[1]
            print("Sales amount: ", montly_sales_data)

            try:
                new_sales_amount = int(input("Enter new amount: "))
                item[1] = new_sales_amount      # convert the second item in the list to the new_sales_amount specified by user
                month = month.title()           # convert back to title case for the print statement
                print("Sales amount for", month, "was modified." )
                write_sales(sales)              # actually update the file (must be closed in other appliations to avoid PermissionError)

            # If user does not enter an integer amount for new_sales_amount:
            except ValueError as e:
                print("ValueError: ", e)
                break  



def display_menu():
    ''' Displays the menu of user commands. '''
    print("COMMAND MENU")
    print("monthly -  View monthly sales")
    print("edit    -  Edit sales for a month")
    print("exit    -  Exit program")
    print()    


def main():

    print()
    print("Monthly Sales program")
    print()
    
    sales = read_sales()
    display_menu()    

    while True:

        print()
        command = input("Command: ")

        if command == "monthly":
            view_monthly_sales(sales)

        elif command == "edit":
            edit(sales)

        elif command == "exit":
            break

        else:
            print("Not a valid command. Please try again.\n")

    print()
    print("Bye!")
    print()


if __name__ == "__main__":
    main()

