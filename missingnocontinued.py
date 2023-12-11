"""
File: missingnocontinued.py
Author: j.jahed@student.rug.nl
Description: This program calculates the length of the longest increasing subsequence possible when removing at most k values from the original sequence. K and the sequence are given by user input
"""

#Since I was unable to submit the last missingo, I used the generated code from Harmen to get the longest increasing subsequence
#File:   missingno.py
#Author: Harmen de Weerd (harmen.de.weerd@rug.nl)
#Function to find the longest increasibg subsequence in an array - assignment 5
def get_longest_increasing_subsequence(array: list[int]) -> int:
   
    current_len = 1
    max_len = 0
    prev= array[0]
    
    for i in range(len(array)):
        current_val = array[i]
        #Checks is current values are greater than the previous values 
        if prev < current_val:
            #updates the length of the current subsequence if it;s greater
            current_len = current_len + 1
        else:
            if  max_len < current_len:
                #if the current length is longer than the max length we update the max length to the current 
                max_len = current_len
            #Reset the length
            current_len = 1
        #update value again to continue the for loop 
        prev = current_val
    
    if max_len < current_len:
        #once the loop is done and the length of the current is bigger than the max subsequent, we update it again
        max_len = current_len
    #returns the length of the longest increasing subsequent 
    return max_len

#Similat function but also uses k as the number of max changes that can be made, given by user input 
def get_length_with_K(user_seq: list[int], k: int) -> int:

    length = len(user_seq)
    #we get the initial longest increasing subsequent
    max_len = get_longest_increasing_subsequence(user_seq)

    #for the case where k is 0 or a vakue smaller, we just return the maximum length obtained in the previous function
    if k <= 0:
        return max_len
    
    #Same case for when the sequent that the user gvies only has 1 or 0 elements , we just smply return the maximum length obtained in the previous function
    if length <= 1:
        return max_len

    #This is a recursive function that removes maximum k numbers from the sequence - I thought using recursion would be the mot optimal way but I get a runtime error unfortunaly...:(
    def remove_numbers(subsequence, k):
        #if the given k is 0 we dont have to do anything, just return the subsequence obtained in the previous function 
        if k == 0:
            return get_longest_increasing_subsequence(subsequence)
        max_result = 0

        #we loop through the subsequence and pop (remove) each element for the length of it to get the maximum length of increasing numbers
        for i in range(len(subsequence)):
            cur_value = subsequence[i]
            subsequence.pop(i)
            #recursion -> k-1 because everytime there's one less k to calculate with 
            cur_length = remove_numbers(subsequence, k - 1)
            #We add the removed number again in the subsequent 
            subsequence.insert(i, cur_value)

            if cur_length > max_result:
                max_result = cur_length

        return max_result

    #first we set this variable to get the longest increasing number of the user subsequent using the first function 
    max_len = get_longest_increasing_subsequence(user_seq)

    #look from 1 to k calculate maximum length with maximum k removals - calls the remove_number function to do that 
    for i in range(1, k + 1):
        current_max_length = remove_numbers(user_seq.copy(), i)
        #If there's a longer sequence, we update the maximum length value everytime by comparing 
        max_len = max(max_len, current_max_length)

    return max_len

#input and output handling by calling functions 
user_seq = list(map(int, input().split(" ")))
k = int(input())
max_len = get_length_with_K(user_seq, k)
print(max_len)
