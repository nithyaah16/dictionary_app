import json

import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

s=True

def translate(w):
    w=w.lower()

    if w.title() in data:
        return data[w.title()]

    elif w in data:
         return data[w]

    elif w.upper() in data:
         return data[w.upper()]

    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if yes, or N if No." % get_close_matches(w,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "The word does not exist. Please double check it or try another word."
        else:
            return "We did not understand your entry. Please try again."

    else:
        return "The word does not exist. Please double check it or try another word."


while s==True:

    print("WELCOME TO THE GREAT ONLINE DICTIONARY!!!")

    word = input("Enter a word: ")

    output=translate(word)

    if type(output)==list:
        for i in output:
            print(i)
        ans=input("Do you want to try again? Enter Y if yes, N if no: ")
        if ans=="Y":
            continue
        elif ans=="N":
            s=False
            print("\n Thank you for using our online dictionary. :) ")
            break
        else:
            print("We did not understand your entry. Please try again.")

    else:
        print(output)
        





