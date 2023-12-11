"""
File: completecycle.py
Author: j.jahed@student.rug.nl
Description: This program determines whether a given input corresponds to a complete cycle or not. If it is a complete cycle, the output should be Yes, otherwise it should be No.
"""

#My function to determine wether it is a complete cycle or not 
def complete_cycle(user_list):
    # List to track which indicies have been visited 
    visited = [] 
    #we start with index 0
    start = 0 

    #Loops through the list 
    for i in range(len(user_list)):
        #checks if the starting index has been visited, if so, not a compelete cycle 
        if start in visited:
            return False  
        #we add the current index to the list 
        visited.append(start) 
        #we update the starting index to thw current index 
        start = user_list[start] 
    # after doing the above process if the starting index is 0, then it shows a complete cycle !!
    return start == 0 

#below just gets the user input (seperated by space as mentioned in the description) and then converts it in a list
user_input = input().split()
user_list = []
for index in user_input:
    user_list.append(int(index))

# Here we just call our functions again to determine if it's a complete cycle or not 
if complete_cycle(user_list):
    print("Yes")
else:
    print("No")