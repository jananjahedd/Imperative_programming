"""
File:  missingvalue.py
Authors: Janan Jahed (s5107318)
Description: A function that finds the missing value in the sequence giving the sequence by finding the difference between each
number in the sequence and binary search
"""

def find_missing(sequence):
    #our start, stop and step variables, the starting number is the first number in the sequence, 
    # the stop is the last, hence and step is the difference between each number calcualuted by the difference between
    #the second and the first number 
    start = 0
    stop = len(sequence) - 1
    step = sequence[1] - sequence[0]
    #The function then loops through the sequence using a while loop
    while start <= stop:
        # This is the implenentatiom of a binary serach, we find the mid point every time and we find the difference between that
        #element and the previous elements - if it is not equal to step that means the missing value is between those values, and we return
        #the index and the value
        mid = (start + stop) // 2
        if sequence[mid] - sequence[mid-1] != step:
            return (mid, sequence[mid-1] + step)
        #This does the same process but with the current element and the next element
        elif sequence[mid+1] - sequence[mid] != step:
            return (mid + 1, sequence[mid] + step)
        #If the current element is in the correct position based on the step and its index, 
        # the function updates start to mid + 1 to search in the upper half of the sequence
        elif sequence[mid] == sequence[0] + mid * step:
            start = mid + 1
        #Otherwise, the function updates the stop to mid - 1 to search in the lower half of the sequence
        else:
            stop = mid - 1