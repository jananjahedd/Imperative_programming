"""
File:  seperatedbydistance.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: A program that counts the number of unique pairs(i, j) in the sequence that are exactly k apart.
"""

# function to count unique pairs with distance k in a sequence
def count_unique_pairs(k, sequence):
    # a dictionary to store the count of each number in the sequence
    count = {}
    # a set to store unique pairs
    unique_pairs = set()

    # loop through the sequence to count how many timesveach number appeared and storing it in the dictionary
    for num in sequence:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # loop through the sequence to find pairs with k difference
    for num in sequence:
        # calculate the possible pairs - it can either be the number minus k difference or plus 
        p1 = num + k
        p2 = num - k

        # check if p1 is in the count dictionary and add the pair to the set unique_pairs
        if p1 in count:
            unique_pairs.add((num, p1))

        # check if k is not zero, and p2 is in the count dictionary, and add the pair to unique_pairs
        if k != 0 and p2 in count:
            unique_pairs.add((p2, num))

    # return the count of unique pairs
    return len(unique_pairs)

# Getting user input and calling the function to calcualte the unique pairs
k = int(input())
sequence = list(map(int, input().split()))
result = count_unique_pairs(k, sequence)
print(result)
