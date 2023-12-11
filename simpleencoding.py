"""
File:  impleencoding.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: A program for encoding a string such that the first character of a text should be shifted by 1 position, the second
character by 2 positions, etc
"""

user_input = input()
encoded = []
temp = 1 

for char in user_input:
    if char.isalpha():
        # For the case where uppercase stays upper and lowercase stays lower
        if char.isupper():
            base = ord('A')
        else:
            base = ord('a')

        # Implementing the shift for alphabets - temp represents the shifting variable which starts with 1
        encoded_char = chr((ord(char) - base + temp) % 26 + base)
        temp += 1
    else:
        #This is for the case of a none letter char, it counts the character in the shifting process but remains the character as it is
        encoded_char = char
        temp += 1

    encoded = encoded + [encoded_char]

#Orders the result string by character using a for loop and then strore it in result which is initially empty 
result = ""
for char in encoded:
    result = result + char
#Prints results
print(result)
