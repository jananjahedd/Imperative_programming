"""
File:  anagramsForPalindromes.py
Authors: Janan Jahed (s5107318)
Description: A program that checks wether a given word is an anagram for a palindrome. 
"""

def is_anagram_for_palindrome(user_input ):
    #convert the input to lower case - for the first test case 
    user_input  = user_input .lower() 
    #https://www.geeksforgeeks.org/python-dictionary/
    #A dictionary to store the count of each character that appears in the string
    char_count = {}
    #Counting the number of characters in a string and adding it to the dictionary - For each character, 
    # we check if it already exists in the count dictionary - If it does, we increase its count by 1 
    for char in user_input :
        if char in char_count:
            char_count[char] += 1
        # If it doesn't, we add it to the dictionary with a count of 1
        else:
            char_count[char] = 1
    #Variable that will hold the number of odd counts 
    odd_count = 0
    #https://www.geeksforgeeks.org/python-dictionary-values/
    # we loop throught the values of count using the built in .values() function in python - for each count we check if it is odd
    # or not - if it is we increment odd_count by 1
    for i in char_count.values():
        if i % 2 != 0:
            odd_count += 1
    #Now we check if the the number of odd counts is greater than 1. If so, then there are more than one characters 
    # with odd counts, meaning the string is not an anagram for a palindrome
    if odd_count > 1:
        return "NO"
    else:
        return "YES"
#We get user input and call the anagram_palindrome function on it
user_input = str(input())
output = is_anagram_for_palindrome(user_input)
print(output)
