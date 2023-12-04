"""
File: addingnumbers.py
Author: j.jahed@student.rug.nl
Description: This program is the implenentation of an arithmetic series in which the user inputs the first and last digit with k being the difference between each digit.
The program calculates the sum of n to m in steps of size k.
"""

def adding_numbers(n, m, k):
    # Base condition - if k is 0 or negative and n > m then it returns 0
    if n > m or k <= 0:
        return 0
    # Initializing the arithmetic sequence formula to solve this problem due to optimality and time limit of 1 sec
    #https://socratic.org/questions/what-is-the-formula-for-the-sum-of-an-arithmetic-sequence
    # Getting the number of terms in the arithmetic sequence 
    num = ((m - n) // k) + 1
    #first term
    term1 = n
    #common difference
    cd = k
    # Using the formula for the sum of an arithmetic series with the common difference 
    result = num * (2 * term1 + (num - 1) * cd) // 2
    return result

#user input 
n, m, k = map(int, input().split())
#calling the function for output 
output = adding_numbers(n, m, k)
#only if it's not equal to 0 then it outputs 
if output != 0:
    print(output)

