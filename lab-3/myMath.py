r'''
    Develop your own math module (myMath) including eight basic functions.
    Function 1: add(x, y)         -> return the summation of x and y
    Function 2: subtraction(x, y) -> return the subtraction between x and y
    Function 3: evenNum(x)        -> return the number of even numbers in the given list
    Function 4: maximum(x)        -> return the maximum value from the given list x
    Function 5: minimum(x)        -> return the minimum value from the given list x
    Function 6: absolute(x)       -> return the absolute value of one number x
    Function 7: sumTotal(x)       -> return the summation of all the elements for a given list x
    Function 8: clear(x)          -> this function sets all the elements into 0 for a given list x

    Write one program (myMain) to import the module you have created to implement 
    the following functions.
    Step 1:
        Input: allows users to input multiple numbers. For simplicity, you can 
               assume all the input numbers are integers.
    Step 2:
        Store all the numbers into one list
    Step 3:
        a. Calculate and print out the difference between the biggest and the 
           smallest number in the list
        b. Calculate and print out the summation between the biggest and the
           smallest numbers in the list
        c. Calculate and print out the summation of all the input numbers in the list
        d. Calculate and print out the number of even numbers in the list
        e. If the smallest number in the list is smaller than 5, set all the 
        value to 0. Otherwise, remain the same. Print all the values in the list in the end.
        
    Hint:
    . To split one string, split() function can be used.
    . For instance, str = '1,2,3,4,10', list1 = str.split(',') would split 
      the string and store the numbers in the list.
    . Please keep in mind that each element in the list is a string type now. 
      You must figure out one way to convert all of them into integer.
'''

import sys

def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def evenNum(x):
    even_count = 0
    
    for num in x:
        if num % 2 == 0:
            even_count += 1
    
    return even_count

def maximum(x):
    max_num = x[0]
    for num in x:
        if num > max_num:
            max_num = num
            
    return max_num

def minimum(x):
    min_num = x[0]
    for num in x:
        if num < min_num:
            min_num = num
            
    return min_num

def absolute(x):
    if x < 0:
        return -x
    else:
        return x
    
def sumTotal(x):
    total = 0
    for num in x:
        total += num
        
    return total

def clear(x):
    for i in range(len(x)):
        x[i] = 0
    
    return x





      
