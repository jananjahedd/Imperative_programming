"""
File: tricky.py
Author: j.jahed@student.rug.nl
Description: This program counts the number of tricky squares between two integers [a,b] given by user input
"""

import math

#First step is to determine wether a number is a perfect square
def perfect_square(user_input):
    #uses the sqrt function from the math library to calculate the sqrt of user input
    sqrt_num = math.isqrt(user_input)
    #checks if the input is the square of the sqrt which shows a perfect square and if so, it return it 
    #https://www.javatpoint.com/how-to-check-for-a-perfect-square-in-python
    return sqrt_num * sqrt_num == user_input

#This function checks if the number is a tricky square 
def is_tricky_square(num):
    #nested function since it can only a tricky square iff it is a perfect square 
    if not perfect_square(num):
        return False

    #Here we convert num into a string so we can count the frequency of each digit occuring 
    number = str(num)
    # Make a counter to count the frequency of a digit occuring in the string - it can be an int from 0 - 9
    digit_count = [0 for _ in range(10)]

    #We count how mant times the digit occured by looping through the string 
    for digit in number:
        digit_count[int(digit)] += 1

    #Variable to check how many dublicates there are since we're only allowed max 1
    repeated = 0
    #This loops checks how many dublicates there are, if it's more than 1 then it's not tricky
    for count in digit_count:
        if count > 1:
            repeated += 1
            if repeated > 1: 
                return False
    #If there's only 1 then it's tricky
    return repeated == 1

#Now we want a function to count how mant tricky squared exists in the range [a,b]
def count_tricky_squares(a, b):
    #make a counter variable 
    count = 0
    ## Loops through perfect squares in the range [1, sqrt(b)+1] - hers it's b**0.5 (sqrt(b)) because otherwise I would get a runtime error since it would loop through uneccessary numbers as well
    for k in range(1, int(b**0.5) + 1):
        num = k * k
        #if the number is in the range and it is a tricky square
        if a <= num <= b and is_tricky_square(num):
            #we add to count!
            count += 1
    return count

#Reading user input (.split because there's a space between a and b), calls the count trickt square to count the number of tricky squared between the two variables 
a, b = map(int, input().split())
result = count_tricky_squares(a, b)
#print the results
print(result)
