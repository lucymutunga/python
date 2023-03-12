# Write your solution below the starter code
# Follow the instructions in the tab to the right
#import random
from random import seed
from random import randint

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

# Make a choice for the computer player
# Get a choice from the user
# Compare the user and computer choice
# Print the right message, based on the choices
options = ["rock","paper","scissors"]
player1_choice = input("player 1, choose rock , paper , or scissors: ")
player2_choice = input("player 2, choose rock , paper , or scissors: ")
if player1_choice not in options or player2_choice not in options:
  print("invalid choice. Please choose rock, paper, or scissors.")
else:
  if player1_choice == player2_choice:
    print("it's a draw!")

  elif(player1_choice == "rock" and player2_choice == "scissors")or\
      (player1_choice == "scissors" and player2_choice == "paper")or\
      (player1_choice == "paper" and player2_choice == "rock"):
      print("player 1 wins!")
  else:
    print("player 2 wins!")