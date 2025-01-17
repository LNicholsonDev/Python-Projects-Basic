# Assignment: Rock Paper Scissors Game Simulator (Assignment 7)
# Class: DEV 108
# Date: 05-22-2024
# Author: Leah Nicholson
# Description: Program which simulates the classic Rock-Paper-Scissors gameplay with two players: a User and the Computer.


# initialize variables as global so they are accessible by multiple functions

import random

count_user_wins = 0
count_computer_wins = 0
count_ties = 0
count_total = 0

def print_welcome():
    '''Prints the welcoming statement and game rules.'''

    print()
    print()
    print("Welcome to Rock/Paper/Scissors Game")
    print()
    print("Rules of the game:")
    print('''  You and the computer will each pick (r)ock, (p)aper, or (s)cissors.
          The winner will be decided using the following policy:
          Rock wins over Scissors but loses to Paper.
          Scissors wins over Paper but loses to Rock.
          Paper wins over Rock but loses to Scissors. 
          
          Let the game begin! Enter 'q' to quit.''')
    print()


def get_user_pick():
    '''Prompts the user for pick (including quit); returns user's pick.'''
    user_pick = (input("Your turn. Pick (r)ock, (p)aper, (s)cissors: "))
    return user_pick


def get_result(user, computer):
    '''Compares the user and computer choices; returns the winner and increments counts.'''

    # Access the global variables in order to update them:
    global count_user_wins
    global count_computer_wins
    global count_ties
    global count_total

    if (user.lower() == 'r') and (computer == 'rock'):
        count_ties += 1
        count_total += 1
        print("You picked r, Computer picked rock")
        print("It's a tie!")
    
    elif (user.lower() == 'r') and (computer == 'paper'):
        count_computer_wins += 1
        count_total += 1
        print("You picked r, Computer picked paper")
        print("Computer wins")

    elif (user.lower() == 'r') and (computer == 'scissors'):
        count_user_wins += 1
        count_total += 1
        print("You picked r, Computer picked scissors")
        print("You win")

    elif (user.lower() == 'p') and (computer == 'rock'):
        count_user_wins += 1
        count_total += 1
        print("You picked p, Computer picked rock")
        print("You win")
    
    elif (user.lower() == 'p') and (computer == 'paper'):
        count_ties += 1
        count_total += 1
        print("You picked p, Computer picked paper")
        print("It's a tie!")
    
    elif (user.lower() == 'p') and (computer == 'scissors'):
        count_computer_wins += 1
        count_total += 1
        print("You picked p, Computer picked scissors")
        print("Computer wins")

    elif (user.lower() == 's') and (computer == 'rock'):
        count_computer_wins += 1
        count_total += 1
        print("You picked s, Computer picked rock")
        print("Computer wins")
    
    elif (user.lower() == 's') and (computer == 'paper'):
        count_user_wins += 1
        count_total += 1
        print("You picked s, Computer picked paper")
        print("You win")
    
    elif (user.lower() == 's') and (computer == 'scissors'):
        count_ties += 1
        count_total += 1
        print("You picked s, Computer picked scissors")
        print("It's a tie!")


def pick_RPS():
    '''Simulates computer picking its choice; returns computer pick as "rock", "paper", or "scissors".'''
    options = ('rock', 'paper', 'scissors')
    computer_pick = random.choice(options)
    return computer_pick


def main():

    print_welcome()                             # displays welcome
    user = get_user_pick()                      # request for user pick 

    while user != 'q':                          # while user does not quit
        computer = pick_RPS()                   # have computer pick a random choice
        winner = get_result(user, computer)     # determine who won and increment apopriate counters
        user = get_user_pick()                  # ask user for more input (another pick or 'q' for quit)

    print("Number of rounds: ", count_total)
    print("Number of times you won: ", count_user_wins)
    print("Number of times Computer won: ", count_computer_wins)
    print("Number of ties: ", count_ties)
    print("Bye!")

main()

