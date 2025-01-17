# Assignment: Pig Latin Translator (Assignment 9)
# Class: DEV 108
# Date: 06-10-2024
# Author: Leah Nicholson
# Description: Program which allows a User to translate English to Pig Latin.


def welcome():
    '''Displays welcome and program title.'''
    print()
    print("Welcome to the Pig Latin Translator")


def clean_text(english_sentence):
    '''Converts to lowercase, splits string into list of strings, and removes punctuation.'''

    # convert to all lowercase
    english_sentence = english_sentence.lower()

    # split string into a list of strings
    english_sentence_list = english_sentence.split()   # default delimiter is white space

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
        
        if word[0] in vowels:       # check if first letter of each word is in the vowels list
            word = word + 'way'     # if starts with vowel, add 'way' to the end
            new_list.append(word)   # add the new revised word to the new_list
            
        else:      # Treat 'y' as a consonant at the start of the word
            
            if word[0] == 'y':
                new_word = word[1:] + word[0] + 'ay'
                
            else:
                # Find first vowel (or 'y') after the first letter
                for i in range(1, len(word)):

                    if word[i] in vowels or word[i] == 'y':     
                        new_word = word[i:] + word[:i] + 'ay'
                        break
                    
                else:
                    # If no vowel (or 'y') found, word should stay unchanged
                    new_word = word + 'ay'
            
            new_list.append(new_word)
    
    restored_sentence = " ".join(new_list)      # put list of words back into one string

    return(restored_sentence)
            

def main():
    '''Runs the program by calling appopriate functions.'''
    welcome()

    choice = 'y'
    while choice.lower() == 'y':

        english_sentence = input("Enter the sentence to be translated: ")
    
        ready_sentence = clean_text(english_sentence)       # takes returned clean_list and holds it in ready_sentence
        restored_sentence = translate_text(ready_sentence)  # send away for translation!

        print("Translated sentence: ", restored_sentence)

        choice = input("Continue? (y/n): ")

    print()
    print("Bye!")


if __name__ == '__main__':
    main()