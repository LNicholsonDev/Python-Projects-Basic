# Assignment: Pig Latin Translator (Assignment 9)
# Class: DEV 108
# Date: 06-10-2024
# Author: Leah Nicholson
# Description: Program which allows a User to translate English to Pig Latin.

def welcome():
    '''Displays welcome and program title.'''
    print()
    print("Welcome to the Piglatin Translator")
    print()

def clean_text(english_sentence):
    '''Converts to lowercase, splits string into list of strings, and removes punctuation.'''

    # convert to all lowercase
    english_sentence = english_sentence.lower()     # string

    # split string into a list of strings
    english_sentence_list = english_sentence.split()         # default delimiter is white space

    # search the string for punctuation and remove it
    punctuation_list = ['?', '.', '!', '"', ',', "'", ':', '\\', '/', '-', ';', '—', '[', ']', '(', ')', '...']
    cleaned_list = []

    for word in english_sentence_list:      # for each of the words in our list of words
         
         for items in punctuation_list:     # for each of the items in the punctuation_list
             
             if items in word:              # if the items in punctuation_list are in the word from our list of words
                 word = word.replace(items, '')        # replace the found punctuation (items) with nothing
         
         cleaned_list.append(word)          # append the new clean word to a clean list

    return cleaned_list


def translate_text(clean_list):
    '''Translates a list that ran through clean_text.'''
    
    
    # manage vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_list = []

    for word in clean_list:
        
        if word[0] in vowels:       # checks if the first letter of each word is in the vowels list
            word = word + 'way'     # if starts with vowel, add 'way'
            new_list.append(word) # add to vowel_list
            
        else:
            for letter in word:
                if letter in vowels:  # find the first vowel
                    word = word[word.index(letter):] + word[:word.index(letter)] + 'ay'
                    new_list.append(word)
                    break
                
            else:
                # If no vowel is found, the word remains unchanged
                new_list.append(word)
                continue

            
            print(new_list)
    







    # # manage vowels
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # vowel_list = []

    # for word in clean_list:
    #     if word[0] in vowels:       # checks if the first letter of each word is in the vowels list
    #         word = word + 'way'     # if starts with vowel, add 'way'
    #         vowel_list.append(word) # add to vowel_list
    #     else:
    #         vowel_list.append(word) # if first letter is consonant, add to vowel_list anyway


    # # manage consonants
    
    # for word in vowel_list:

    #     if word[0] not in vowels:      # not in vowels means a consonant

    #         for letter in vowels:
    #             first_vowel_index = word.find(letter)

    #             if first_vowel_index != -1:         # if the vowel is found
    #                 word = word[first_vowel_index:] + word[:first_vowel_index] + 'ay'
                    


def print_translation():
    '''Prints the translated text (the Pig Latin).'''
    print()


def main():
    '''Runs the program by calling appopriate functions.'''

    welcome()
    english_sentence = input("Enter the sentence to be translated: ")
    
    ready_sentence = clean_text(english_sentence)       # takes returned clean_list and holds it in ready_sentence
    translate_text(ready_sentence)                      # send away for translation!




if __name__ == '__main__':
    main()