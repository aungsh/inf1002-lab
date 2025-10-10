r'''
Task Description: 
     A word is considered elfish if it contains the letters: e, l and f in it, in any 
     order. For instance, we would say that the following words are elfish: tasteful, 
     whiteleaf, unfriendly and waffles, because they each contain those letters. Use 
     the recursive function to implement this. Write one program to call your recursive 
     function and tell the user whether the input word is one elfish or not. 
     
     HINT: You can recursively reduce both the elfish letters and input word. 
     The sample executions are provided as follows:

Note: 
     Your output should be in ONE line

Running example: 
     C:\INF1002\Lab4\elfish> python3 elfish.py waffles
     waffles is one elfish word!

     C:\INF1002\Lab4\elfish> python3 elfish.py instance
     instance is not an elfish word!
'''

import sys

# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def is_elfish(word, letters="elf"):
    if letters == "":
        return True
    if word == "":
        return False
    if word[0] in letters:
        letters = letters.replace(word[0], "")
    return is_elfish(word[1:], letters)

def elfish():
    word = sys.argv[1].lower()
    if is_elfish(word):
        print(f"{word} is one elfish word!")
    else:
        print(f"{word} is not an elfish word!")

if __name__=='__main__':
     elfish()
      
