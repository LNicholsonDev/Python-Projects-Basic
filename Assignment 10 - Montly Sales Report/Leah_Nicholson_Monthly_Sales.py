# Assignment: Monthly Sales Report (Assignment 10)
# Class: DEV 108
# Date: 06-14-2024
# Author: Leah Nicholson
# Description: Program which reads average montly sales data from a .csv file and displays content to User.
    # User may update the montly sales value for any given month - data changes are persistent (the .csv file updates).
# SPECIAL note: The main page to the assignment says to also calculate the total yearly sales, but the instruction pdf does not mention this.
    # I have omitted the yearly calculation since it was not part of the starter code. 


#!/usr/bin/env python3

import csv              # I did not use the sys module, so I removed the other import

# a file in the current directory
FILENAME = "monthly_sales.csv"

# helper list
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def read_sales():
    ''' Function to read contents of .csv FILENAME and return the contents as list of lists. '''

    with open(FILENAME, newline = "") as file:

        data_list = []                  # needed to capture, store, and return the file data
        contents = csv.reader(file)

        for row in contents:
            row[1] = int(row[1])        # convert each of the second items (the dates) from strings to integers
            data_list.append(row)       # append the whole row of data to the new list (for each row in contents)
        
    return data_list                    # actually return the data so it can be used


def write_sales(sales):
    ''' Function to write the contents of sales (a list of lists) to FILENAME. '''

    with open(FILENAME, "w", newline = "") as file:

        writer = csv.writer(file)
        writer.writerows(sales) 


def view_monthly_sales(sales):
    ''' Function to print the monthly sales values. '''

    print()

    for item in sales:
        print(item[0], " - ", item[1])


def edit(sales):
    ''' Lets user edit the sales value for one of the months using 3-letter month code.'''

    # Raise ValueError if the User enters an invalid month
    try:
        month = input("Three-letter month: ")
        month = month.lower()                   

        if month.title() not in MONTH_NAMES:        # casts the user input into title case to check the MONTH_NAMES list
            raise ValueError                        # lines 63-67 skipped if month.title() IS in the MONTH_LIST

    except ValueError:
        print("ValueError: Invalid three-letter month.")


    # if user enters a valid month
    for item in sales:
                
        if item[0].lower() == month:        # makes the item in the list lowercase
                    
#            montly_sales_data = item[1]
#            print("Sales amount: ", montly_sales_data)      # seems right to display current value before prompting for change

            try:
                new_sales_amount = int(input("Enter new sales amount: "))
                item[1] = new_sales_amount      # convert the second item in the list to the new_sales_amount specified by user
                month = month.title()           # convert back to title case for the print statement
                print("Sales amount for", month, "was modified.")
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


def main():
    '''Calls other functions to execute program.'''

    print()
    print("Monthly Sales Program")
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

        else:       # if command is not in the menu, prompt again for a valid command
            print("Not a valid command. Please try again.\n")

    print()
    print("Bye!")
    print()


if __name__ == "__main__":
    main()