import json
from difflib import get_close_matches

words_data = json.load(open("data.json"))

word = input("Enter a word :")

def word_meaning(word):
  
  
    word = word.lower()
    
    
    if word in words_data:
        return words_data[word]
      
   
    elif word.title() in words_data:
        return words_data[word.title()]
      
   
    elif word.upper() in words_data:
        return words_data[word.upper()]
      
    
    elif len(get_close_matches(word, words_data.keys())) >0:
      
       
        similar_words_list = list(map(str, get_close_matches(word, words_data.keys())))
        
       
        ans = input("Did you mean %s instead? Enter 'Y' If yes or 'N' if No  :" % similar_words_list)
        
        if ans.lower() == 'y':
           
            index = input("\nEnter the position number of word to select the word. Ex 1 or 2 or 3 : ")
            return word_meaning(get_close_matches(word, words_data.keys())[int(index)-1])
        elif ans.lower() == 'n':
            print("Word Doesnt exists. Please re-check it!!!")
        else:
            print("Sorry, We don't understand you!!!!")
    else:
        print("Word Doesnt exists. Please re-check it!!!")

meaning = word_meaning(word)

if type(meaning)==list:
    for item in meaning:
        print("\nMeaning :",item)
        print("\n")
else:
    print("\nMeaning :",meaning)

