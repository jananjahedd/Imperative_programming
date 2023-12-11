"""
File: rockpaperscissors.py
Author: Janan Jahed (j.jahed@student.rug.nl)
Description: If both players pick the same action, the game ends in a draw. Otherwise, ‘rock’ beats ‘scissors’, ‘scissors’ beats ‘paper’, and ‘paper’
beats ‘rock’
"""
#Gets the user input
player1 = input()
player2 = input()

#If both players say the same thing then it's a draw
if (player1 == player2):
    print("It is a draw.")

#The 3 conditions for a player1 to win described in the file
elif ((player1.lower() == "rock" and player2.lower() == "scissors") or (player1.lower() == "scissors" and player2.lower() == "paper") or  (player1.lower() == "paper" and player2.lower() == "rock")):
    print("Player one wins.")

#In any other case player 2 wins because it will be the opposite way
else:
    print("Player two wins.")