"""
File:  joiningforces.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: This program gets as input a number of sorted sequences and outputs the sorted
 sequence that consists of all the input sequences.
"""

# a function to combine sorted sequences
def combine_sorted_sequences():
    # an empty list to store the sequences
    seq = []
    
    #  get input until an empty line is entered
    while True:
        #https://www.geeksforgeeks.org/python-string-strip/
        sequence = input().strip()
        
        # break the loop if an empty line is encountered
        if sequence == "":
            break
        
        # append each sequence as a list of integers to the seq list
        seq.append(list(map(int, sequence.split())))
    
    # combine all values from input sequences into a single list
    all_values = []
    for sequence in seq:
        #https://stackoverflow.com/questions/8177079/take-the-content-of-a-list-and-append-it-to-another-list
        #https://www.w3schools.com/python/python_lists_add.asp    to add the elements of the sequence list to the all_values list
        all_values.extend(sequence)
    
    # sort the combined list of values with the python sort() function
    #https://www.w3schools.com/python/ref_list_sort.asp
    all_values.sort()
    
    # return the sorted list of values
    return all_values

# call the sorted funcntion and ouput the numbers 
result = combine_sorted_sequences()
#https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
#we need to unpack the elements of the list into individual elements otheriwise it will print the list format
print(*result)

