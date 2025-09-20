r'''
Task Description:
In this task, you are going to design one program to check the popular characters
in a given string. You need to write one program to calculate the top 5 most 
frequent characters. The following are some hints that may help you design this program. 
	. String has a cool function that you can use to return a copy of the string 
     in which all case-based characters have been lowercased. 
	. To get the top 5 most frequent characters after sorting them, you need to 
     extract all the characters first and figure out one way to calculate the frequency 
     of each character. Then select the top 5 characters. 
	. The output must in the descending order of character frequency. If there are 
     characters with the same frequency, they must be printed in ascending ASCII order.
	. Print out the top 5 characters and their counts in the screen. (Your output should be in one line)
     do not use lambda

Running Examples:
C:\INF1002\Lab2\CountPopularChars>python3 CountPopularChars.py sdsERwweYxcxeewHJesddsdskjjkjrFGe21DS2145o9003gDDS
d:7,s:7,e:6,j:4,w:3
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def CountPopularChars():
     lower = sys.argv[1].lower();
     char_list = list(lower)
     
     char_dict = {}
     for char in char_list:
          if char in char_dict:
               char_dict[char] += 1
          else:
               char_dict[char] = 1
               
     # sorted_dict = {}
     # for char in char_dict:
     #      for char2 in sorted_dict:
               
     items = []
     for key in char_dict:
          items.append((key, char_dict[key]))
          
     for i in range(len(items)):
          for j in range(i + 1, len(items)):
               if items[i][1] < items[j][1] or (items[i][1] == items[j][1] and items[i][0] > items[j][0]):
                    items[i], items[j] = items[j], items[i]
          
     top_five = []
     for i in range(min(5, len(items))):
          top_five.append(f"{items[i][0]}:{items[i][1]}")
          
     print(','.join(top_five))
     
if __name__=='__main__':
      CountPopularChars()
      
