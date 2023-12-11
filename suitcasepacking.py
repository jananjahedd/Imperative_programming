"""
File: suitcasepacking.py
Author: j.jahed@student.rug.nl
Description: This program gets the number of items, volume of the suitcase, size of item and its satisfcation from the user input
and find the optimal satisfaction value that can be achieved from a set of items that fit inside the suitcase.
"""
#Recursive function
def optimal_satisfaction(n, v, size, satisfaction):
    #Base-case , when no items and volume is 0 then it's 0
    if (n == 0 or v == 0):
        return 0
    #If the size of the current item is greater than the remaining volume, then it can't be added (n-1 because of recursion call)
    if size[n - 1] > v:
        return optimal_satisfaction(n - 1, v, size, satisfaction)
    #Now we have two cases, one if we add the current item and two if we don't add the current item. - the first case 
    #basically adds the satisfaction obtained with the current item  to the reduced volume, here we reduce the volume by the size
    #of the current item because we assume that the current size is a part of the volume when doing recursion 
    added_satisfaction = satisfaction[n - 1] + optimal_satisfaction(n - 1, v - size[n - 1], size, satisfaction)
    #and if we don't add the item it just gets the optimal satisfaction of the suitacse without that item - both cases use recursion
    #to get the optimal satisfaction!
    removed_satisfaction = optimal_satisfaction(n - 1, v, size, satisfaction)
    #Now we check which case yields a higher value 
    return max(added_satisfaction, removed_satisfaction)

#We get the number of items and volume from the user 
n, v = map(int, input().split())
#we initialize and array for size and satisfaction since it will hold multiple numbers
size = []
satisfaction = []

#The process of initializing what is size and what is satisfaction - usage of counter to ensure we don't exceed the  number of items 
counter = 0
while counter < n:
    item_descriptions = input().split()
    #Here we append the first index of the array to size and second to satsisfaction and we just simply don't do anything with 0th
    size.append(int(item_descriptions[1]))
    satisfaction.append(int(item_descriptions[2]))
    #incremenet the counter - so by the end of this loop we will have up to n size and satisfaction values in our arrays
    counter += 1
#we cann our recursive function to calculate the optimal satisfaction using user inputs 
result = optimal_satisfaction(n, v, size, satisfaction)
print(result)
