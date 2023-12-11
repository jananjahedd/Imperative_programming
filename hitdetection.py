"""
File: hitdetection.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: Given the coordinates of a rectangle and of a point, the program calculates whether the point lies within the rectangle or not.
"""

#These are the sets of inputs for the coordinates of the rectangle 
xAxis1 = int(input())
yAxis1 = int(input())
xAxis2 = int(input())
yAxis2 = int(input())

#These are the sets of inputs of the coordinates of the points
userInput1 = int(input())
userInput2 = int (input())

#If the coordinates of the points is between the coordinates of the trectangle then it's inside it
if ((xAxis1 < userInput1 < xAxis2 or xAxis1 > userInput1 > xAxis2) and (yAxis1 < userInput2 < yAxis2 or yAxis1 > userInput2 > yAxis2)): 
    print ("INSIDE")

#If (one of) the coordinates of the points are the same as (one of) the coordinates of rectangle then that point is on edge 
elif (xAxis1 == userInput1 or xAxis2 == userInput1 or yAxis1 == userInput2 or yAxis2 == userInput2):
    print("EDGE")
#In any other case the point will be outside the rectangle
else:
    print("OUTSIDE")