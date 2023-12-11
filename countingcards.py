"""
File: countingcards.py
Author: j.jahed@student.rug.nl
Description: This program find the total number of combinations for h cards wih d distict 
labels and num_d_cards number of distict labels using user input 
"""


def combination(h, d, num_d_cards):
    #base case for when we only have one distict card, makes sure we have enough cards to form h
    if d == 1:
        if num_d_cards[0] >= h:
            return 1
        else:
            return 0
    #if we have more than 1 distict cards, we can recursively find the number of combinations
    #We split the distict cards in 2, then recursivley find the combination for each half and then we multiply them
    #together to get all the possible combinations of cards with d distinct labels 
    count = 0
    for i in range(h + 1):
        first_params = (i, d // 2, num_d_cards[:d // 2])
        first_half = combination(*first_params)
        #h-i and d - d // 2 because we have to find the remaining of those values 
        second_params = (h - i, d - d // 2, num_d_cards[d // 2:])
        second_half = combination(*second_params)
        #counting the combination of independant steps 
        count += first_half * second_half
    
    return count

#Getting user input using the spli function and map and printing the results by calling the function on it 
h, d = map(int, input().split())
num_d_cards = list(map(int, input().split()))
result = combination(h, d, num_d_cards)
print(result)
