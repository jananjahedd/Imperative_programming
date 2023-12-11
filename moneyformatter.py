"""
File: moneyFormatter.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: A program that formats float numbers in terms of euros and cents
"""

#Creating and empty array to store the user input 
userArr = [] 
# Read user inputs 
user_input = input()
#stores the user number (float because decimal) in the array 
userArr.append(float(user_input))

# Calculates the number in cents
answer = int(sum(userArr) * 100)

# Converts that number to euros
fullEuro = answer // 100

# Gets the exact number of cents 
fullCents = answer % 100

# Print the amount of euros and cent
print(f"{fullEuro} euro {fullCents}")


