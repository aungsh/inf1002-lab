r'''
Task Description:
      In this task, you are going to develop a letter game to count the number of leters
      in the given string.
      Step1:
            Write one functon leter_count(str) that take in one word and returns a dictonary 
            with the frequency counts of the various letters. Upper and lower-case characters 
            are different characters.
            Sample executon:
                  >>letter_count('This')
                  { 'h':1, 'T':1, 'i':1, 's':1}
                  >>letter_count('Thisisit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
      Step 2:
            Write one functon double_count(str1, str2) that takes in two words and returns a 
            dictonary with the frequency counts of the various le􀆩ers. Upper and lower-case 
            characters are different characters.
            Sample executon:
                  >> double_count('This', 'isit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
      Step 3:
            Write one functon various_count(*str) that takes in any number of words and returns 
            a dictonary with the frequency counts of the various le􀆩ers. Upper and lower-case 
            characters are different characters.
            Sample execu􀆟on:
                  >> various_count('This')
                  { 'h':1, 'T':1, 'i':1, 's':1}
                  >> various_count('This', 'isit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
                  >> various_count('This', 'is, 'it')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
            HINT: In Python, using “def func(*str): list1=str”, list1 can obtain any number of 
            arguments and stores it as a list. You can further get each element from the list 
            and count each word independently. You can implement another func􀆟on to merge two 
            dictonaries. 
            Below is an example:
                  >> def str1(*str)
                        list = str
                        print list
                  >> str1('This', 'is', 'so', 'cool')
                  ('This', 'is', 'so', 'cool')

      Step 4:
            Write one program to allow users to input different number of words and output each
            character's frequency.
            Some of codes read as follows. Please print your results in the characters' ASCII 
            descending order according to this format:

            for item in sorted_total:
            print ('%s:%d' % (item, total[item]), end=' ')

            Note that the following running example is in ONE line, and your output should be in ONE line.

      Running example:
      C:\INF1002\Lab3\CountingLetters>python3 CountLetters.py Firefox,is,having,trouble,recovering,your,windows,and,tabs
      y:1 x:1 w:2 v:2 u:2 t:2 s:3 r:5 o:5 n:4 l:1 i:5 h:1 g:2 f:1 e:4 d:2 c:1 b:2 a:3 F:1

'''
import sys

# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

#1
def letter_count(tmpStr):
      letter_dict = {}
      letters_list = list(tmpStr)
      for letter in letters_list:
            if letter in letter_dict:
                  letter_dict[letter] = letter_dict[letter] + 1
            else:
                  letter_dict[letter] = 1
                  
      return letter_dict            
      
#2 this function, there are two input arguments: two strings
def double_count(str1, str2):
      dict1 = letter_count(str1)
      dict2 = letter_count(str2)
      combined_dict = {}
      for key, value in dict1.items():
            if key in dict2:
                  combined_dict[key] = dict1[key] + dict2[key]
            else:
                  combined_dict[key] = value
                  
      for key, value in dict2.items():
            if key not in combined_dict:
                  combined_dict[key] = value
                  
      return combined_dict

#3 This one takes only one input argument
def various_counts(*tmpStr):
      combined_dict = {}
      for word in tmpStr:
            dict1 = letter_count(word)
            for key, value in dict1.items():
                  if key in combined_dict:
                        combined_dict[key] = dict1[key] + combined_dict[key]
                  else:
                        combined_dict[key] = value
                        
      return combined_dict
      
def CountLetters():
      tmpstr = sys.argv[1]
      word_list = tmpstr.split(",")
      combined_dict = various_counts(*word_list)
      sorted_dict = dict(sorted(combined_dict.items(), reverse=True))
      for item in sorted_dict:
            print ('%s:%d' % (item, sorted_dict[item]), end=' ')
      
if __name__=='__main__':
      CountLetters()