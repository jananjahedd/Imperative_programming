"""
File: columnar.py
Author: j.jahed@student.rug.nl
Description: This program implements a columnar transposition in a way that it gets the the text to be encoded,and the
sequence of the digits 1 through n that indicate the order of shich the columns should be read and encoded.
"""

# This function has a nested function that preforms the encryption process within it and the function itself is responsible for making the correct matrix to print the encrypted text
def columnar_encryption(text, column_order):
    
    text_len = len(text)
    #https://runestone.academy/ns/books/published/fopp/Sequences/TheSliceOperator.html
    # this trims the string column_order to the value of text_len - test case 3, so it doesnt consider empty cells after the string as space
    column_order = column_order[:text_len]
    # Each character in the string becomes an element in the list/ individual characters.
    text_lst = list(text)
    matrix = []

    #This is for the test case when no text has been entered. It just returns nothing 
    if len(text) == 0:
        return ""
    # Here I made a function that recursively encrypts the text - This shows the encryption logic 
    def encryption(text, column_order, indx, result):
        #The base case
        if indx == len(column_order):
            return result
        #Here I sort the column in ascending order and then find the current index of the column to be read at each step of the process
        sorting_column = sorted(list(column_order))
        current_index = column_order.index(sorting_column[indx])
        #Looping through the matrix rows and adding the character in that index to the result
        for row in matrix:
            if current_index < len(row):
                result += row[current_index]
        # Recursively calling the function for the next columns - makes the code efficient and more presentable, also thsi week's content
        return encryption(text, column_order, indx + 1, result)

    #Iterate through the text_lst in chunks of the length of column_order and create a matrix with rows 
    for i in range(0, len(text_lst), len(column_order)):
        # #https://runestone.academy/ns/books/published/fopp/Sequences/TheSliceOperator.html
        # Adding the sliced text_lst (characters of the text_lst) to matrix row
        matrix.append(text_lst[i:i + len(column_order)])

    #Again recursively calling the encryption function for getting the result of each encryitpion starting from index 0
    result = encryption(text, column_order, 0, "")
    return result

#Asking for user input and printing the result 
text = input()
column_order = input()
result = columnar_encryption(text, column_order)
print(result)
