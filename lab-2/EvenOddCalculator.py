r'''
Task Description:
In this task, you are assigned to develop one program to help users calculate 
different information based a series of user provided numbers (integers). 
Detailed requirement is provided as follows: 

Input: A series of numbers 
Output: (Your output should be in one line)
	. The summation of the even numbers and summation of the odd numbers in 
       the input list 
	. The difference between the biggest and smallest numbers in the input list
	. The count of even numbers and odd numbers in the input list
	. The "centered" average of the list of integers. The centered average can be 
       calculated as the mean average of the values, after removing the largest and 
       smallest values in the array. If there are multiple copies of the smallest 
       value, ignore all but keep just one copy, and likewise for the largest value. 
       For instance, [12,2,8,7,100] -> 9; [2,2,8,11,100] -> 7

To have a better understanding of the loops, please try to implement 
two programs: one uses "for" and another uses "while" loop.

Running Examples:

C:\INF1002\Lab2\EvenOddCalculator> python3 EvenOddCalculator.py 12,2,8,7,100
The sum of all even numbers is 122, the sum of all odd numbers is 7, the difference between the biggest and smallest number is 98, the total number of even numbers is 4, the total number of odd numbers is 1, the centered average is 9.

C:\INF1002\Lab2\EvenOddCalculator> python3 EvenOddCalculator.py 1,2,abcd,8,11,200,301
Please enter valid integers.
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def EvenOddCalculator():
       str_list = sys.argv[1].split(",")
       
       sum_even = 0
       count_even = 0
       sum_odd = 0
       count_odd = 0
       biggest = 0
       smallest = 0
       total = 0
       
       try:
              for str in str_list:
                     num = int(str)
                     total += num
                     if num > biggest:
                            biggest = num
                     if num < smallest or smallest == 0:
                            smallest = num
                     if num % 2 == 0:
                            count_even += 1
                            sum_even += num
                     else:
                            count_odd += 1
                            sum_odd += num
                            
              big_small_diff = biggest - smallest
              centered_avg = (total - biggest - smallest)/(len(str_list)-2)
              
              print(f"The sum of all even numbers is {sum_even}, the sum of all odd numbers is {sum_odd}, the difference between the biggest and smallest number is {big_small_diff}, the total number of even numbers is {count_even}, the total number of odd numbers is {count_odd}, the centered average is {int(centered_avg)}.")
       except ValueError:
              print("Please enter valid integers.")
              return

if __name__=='__main__':
      EvenOddCalculator()
      
