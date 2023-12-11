"""
File:  primechoice.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: A program that prints the nth prime number in an ordered list of primes given n is the user input. 
"""


#function to check if the number is a prime - I implemented this in primeexamples.py and I'm re-using my own code
def isPrime(n):
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

#function to find the nth prime 
def nThPrime(n):
    count = 0
    start = 2

    #we loop until n and find the nth prime by first making sure the number we encounter
    # is a prime and then incrementing our count and start value until it reaches n
    while count < n:
        if isPrime(start):
            count += 1
        start += 1
    #since we start with 2, we should make sure that correct nth term is found because 
    #the loop increments start before checking if the current number is prime - we have 1 more than what we need

    return start - 1

#We get the user input and call the nthPrime function to find the nth prime and print the results 
inp = int(input())
result = nThPrime(inp)
print(result)
