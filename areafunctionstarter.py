
"""
File: area.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: A program that calculates the area of a rectangle and the area of a triangle.
"""
#This gets the first input in which the user says wether it's a triangle or rectangle
userInput = input()

#Function for calculating the area of triangle in float (because of decimals -> x.5)
def get_area_of_triangle():
    base = float(input())
    height = float(input())
    areaTriangle = (base * height) / 2
    print (areaTriangle)

#Function for calculating the area of rectangle in float (because of decimals -> x.5)
def get_area_of_rectangle():
    length = float(input ())
    width = float(input())
    areaRectangle = (length * width)
    print (areaRectangle)

#if the user types in triangle, calls the function related to calculating the area of the triangle
#.lower is a function that converts the user input all to lower case so the program isnt limited to only one case of typing:
#https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
if userInput.lower() == "triangle":
   get_area_of_triangle()

#else if the user types in rectangle, calls the function related to calculating the area of rectanle
if userInput.lower() == "rectangle":
    get_area_of_rectangle()




