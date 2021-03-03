# -*- coding: utf-8 -*-

import json
from difflib import get_close_matches

data=json.load(open("data.json"))
word=input("Enter word to search :")

def getMeaning(w):
   
    w = w.lower()
    
    if w in data:
        return data[w]
    
    elif len(get_close_matches(w,data.keys())) > 0:
        match = get_close_matches(w,data.keys())[0]
        print("Did you mean %s instead? Enter Y if yes or N if no: " %match)
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            return data[match]
        elif choice == 'n':
            return "The word doesn't exist. Please re-check it."
        else:
            return "Sorry, We didn't understand your entry."
    else:
        return "The word doesn't exist. Please re-check it."

meaning = getMeaning(word)

if type(meaning)==list:
    for item in meaning:
        print("Meaning :",item)
        print("\n")
else:
    print("Meaning :",meaning)




