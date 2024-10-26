# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."
from html.parser import charref


# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here
    Result = ''

    User_input = input('Enter a sentence with no spaces but uppercase the first letter of every word: ')

    Result = Result + User_input[0]

    for i in range (1, len(User_input)):
        char = User_input[i]
        if char.isupper():
            Result += ' ' + char.lower()
        else:
            Result += char.lower()

    return Result



# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)