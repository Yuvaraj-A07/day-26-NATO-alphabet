
#TODO 1. Create a dictionary in this format:

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

letter_dict = {row.letter: row.code for index, row in data.iterrows()}
# print(letter_dict)


l = list(letter_dict.keys())
is_ok = True
while is_ok:
    try:
        name = input("Enter word : ").upper()
        phonetic = [letter_dict[letter] for letter in name]
    except KeyError:
        print("sorry, only letters in the alphabet")
    # for letter in name:
    #     if(letter in l):
    #         phonetic.append(letter_dict[letter])
    else:
        is_ok = False
        print(phonetic)

# letter_list = [value for key, value in letter_dict.items() if key in word]
