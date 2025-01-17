#!/usr/bin/env python3

import csv
import sys

# a file in the current directory
FILENAME = "monthly_sales.csv"
# helper list
MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def read_sales():
    ''' Function to read contents of FILENAME and return the contents as
list of lists. Since csv returns string values for all columns, function
should convert the sales number to integers.'''
    pass
def write_sales(sales):
    ''' Function to write the contents of sales, a list of lists, to 
FILENAME.'''
    pass

def view_monthly_sales(sales):
    ''' Function to print the monthly sales values.
'''
    pass

def edit(sales):
    ''' Let user edit the sales value for one of the months.
    - Prompt the user for 3-letter month code. Raise an exception if user enters an
        invalid code. 
    - Prompt the user for the new sales numbers.
    - Use a try/except block that will handle invalid input in both the cases.
    '''
    pass

def display_menu():
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("edit    - Edit sales for a month")
    print("exit    - Exit program")
    print()    

def main():
    print("Monthly Sales program")
    print()
    
    sales = read_sales()
    display_menu()    
    while True:
        command = input("Command: ")
        if command == "monthly":
            view_monthly_sales(sales)
        elif command == "edit":
            edit(sales)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
