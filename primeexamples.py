"""
File:  primeexamples.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: A program that prints the largest prime smaller than the user input. 
"""

# Function that checks whether a number is prime or not - source to help: cover goodiebag.c
def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to get the largest prime number smaller than the user input - keeps decreasing the number by 1 until it finds a prime.
def previous_prime(user_input):
    user_input = user_input- 1 
    while user_input > 1:
        if is_prime(user_input):
            return user_input
        user_input = user_input - 1

# Get user input
user_input = int(input())

# Call the function to find the largest prime
answer = previous_prime(user_input)
print(answer)

