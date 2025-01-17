# Assignment: Contacts Manager (Assignment 8)
# Class: DEV 108
# Date: 06-05-2024
# Author: Leah Nicholson
# Description: Program which allows a User to manage the email addresses and phone numbers for contacts.
# Can display all contact names, add a new contact, view a contact, edit a contact, or delete a contact.


def display(names):
    """ Displays the contact names. """

    list_number = 1         # provides the listed numbers (eg: 1., 2., ...) in the displayed names

    if (names == []):       # if empty list of contacts
        print("There are no contacts in the list.")
        print()

    else:

        for name in names:      # for each name in the list, print that name with a number from list_number and a period
            print(str(list_number) + ". " + name)
            list_number += 1    # increase the list number by 1 after each iteration
        
        print()
    

def add(names, emails, numbers):
    '''Adds a new contact name.'''
    
    new_name = input("Name: ")          # gather info from User for the added contact
    new_email = input("Email: ")
    new_number = input("Phone: ")
    
    names.append(new_name)              # lists are mutable - can just append directly to passed list arguments
    emails.append(new_email)
    numbers.append(new_number)

    print(new_name + " was added.")     # reference the new name that was added
    print()


def view(names, emails, numbers):
    '''View the contact name and details when a contact list number (eg: 1., 2., ...) is specified.'''
    
    contact_list_number = int(input("Number: "))
    index = contact_list_number - 1         # accomodates the fact that index starts at zero
    
    if (index < 0) or index >= len(names):  # checks if contact number is < 0 or if index is out of range
        print("Invalid contact number.")
        print()
        return                              
    
    else: 
        print("Name: ", names[index])       # index into the list to retrieve data from each list
        print("Email: ", emails[index])
        print("Phone: ", numbers[index])
        print()
    

def delete(names, emails, numbers):
    '''Deletes the contact.'''

    contact_list_number = int(input("Number: "))
    index = contact_list_number - 1

    if (index < 0) or index >= len(names):
        print("Invalid contact number.")
        print()
        return
    
    else:

        removed_name = names[index]     # stores the removed name in a variable for later reference

        names.pop(index)                # removes specified contact name/email/phone by indexing based on contact_list_number
        emails.pop(index)               
        numbers.pop(index)
    
        print(removed_name + " was deleted.")
        print()


def edit_phone(names, emails, numbers):
    '''Edits the contact's phone number.'''
    
    contact_list_number = int(input("Number: "))
    index = contact_list_number - 1

    if (index < 0) or index >= len(names):
        print("Invalid contact number.")
        print()
        return
    
    else:

        new_phone = input("New phone number: ")
        edited_name = names[index]

        numbers.pop(index)                      # indexing and removing the phone number
        numbers.insert(index, new_phone)        # inserting in the new phone number at same list position
        print(edited_name + "'s phone number was edited.")
        print()
    

def show_title():
    '''Show the title of the program.'''

    print()
    print("Contact Manager")
    print()


def show_menu():
    '''Show the menu of prompts available to the User.'''

    print("COMMAND MENU")
    print("list - Show all contacts", end = "\t")
    print("view - View a contact")
    print("edit - Edit phone number", end = "\t")
    print("add - Add a contact")
    print("del - Delete a contact", end = "  \t")
    print("exit - Exit program")
    print()


def main():
    '''Calls the functions of the program.'''

    contacts_names = ["Harry Potter","Ron Weasley"]
    contacts_emails = ["hpotter@hogwarts.edu","rweasley@hogwarts.edu"]
    contacts_numbers = ["+44 20 6789 0022", "+44 20 2345 0958"]

    show_title()
    show_menu()

    while True:

        command = input("Command: ")

        if command == "list":
            display(contacts_names)

        elif command == "view":
            view(contacts_names, contacts_emails, contacts_numbers)

        elif command == "add":
            add(contacts_names, contacts_emails, contacts_numbers)
            
        elif command == "del":
            delete(contacts_names, contacts_emails, contacts_numbers)

        elif command == "edit":
            edit_phone(contacts_names, contacts_emails, contacts_numbers)

        elif command == "exit":
            break

        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")


if __name__ == "__main__":
    main()