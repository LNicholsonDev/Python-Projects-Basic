# Assignment: Rhymes (Assignment 6)
# Class: DEV 108
# Date: 05-19-2024
# Author: Leah Nicholson
# Description: Program which creates a famous rhyme, using functions to print the lyrics.

def print_refrain():
    '''Prints the first two lines of the poem.'''

    print("Old MacDonald had a farm")
    print("Ee i ee i o")

def print_verse(animal_name, animal_sound):
    '''Receives animal name (plural) and animal sound, then prints individual verse. Example: (cats, meow)'''

    print_refrain()     # note: Not print(print_refrain()) - prints location, not function contents
    print("And on his farm he had some", animal_name)
    print("Ee i ee i o")
    print("With a ", animal_sound, "-", animal_sound, " here", sep = "")
    print("And a ", animal_sound, "-", animal_sound, " there", sep = "")
    print("Here a ", animal_sound, ", there a " , animal_sound, sep = "")
    print("Everywhere a ", animal_sound, "-", animal_sound, sep = "")
    print_refrain()
    print()

def main():
    '''Calls print_verse() to display the full poem with three verses.'''

    print()
    print('    "Old MacDonald"')      # prints the title once (not in duplicated code above)
    print()
    print_verse("cows", "moo")      # passed arguments directly (no need for variables)
    print_verse("chicks", "cluck")
    print_verse("ducks", "quack")
    print()

main()
