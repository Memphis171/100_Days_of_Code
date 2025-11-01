# took the main.py file from day 26 and pasted below to improve
import pandas as pd

#read  the data  with pandas
data = pd.read_csv("../Day_26_List_Comprehension_NATO_Alphabet/nato_phonetic_alphabet.csv")


#create a new dictionary from the dataframe
letter_dict = {row.letter:row.code for (index,row) in data.iterrows()}


def  generate_phonetic():
    # get a word from the user and make sure it is upper case to match the new dictionary
    word = input("Enter a word: ").upper()
    try:
        # create a new list using the nato alphabet iterating off the word
        letter_code = [letter_dict[letter] for letter in word]
    except KeyError:
        print("Please use only letters.")
        generate_phonetic()
    else:
        print(letter_code)

generate_phonetic()