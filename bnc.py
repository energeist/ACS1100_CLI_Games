# Import randint function from random module
from random import randint

# Define roles in a dictionary
roles = ["bear", "ninja", "cowboy"]

# Initialize variables
player = False
score = 0

print("")
# Ask if instructions are required
instructions = input("Welcome to Bear, Ninja, Cowboy!  Would you like instructions? (yes/no) > ")
# Check input
while instructions.lower() != "yes" and instructions.lower() != "no":
    instructions = input("Instructions unclear... Please answer with 'yes' or 'no' only > ")
if instructions.lower() == "yes":
    print("")
    print("""The rules of the game are as follows:
You and the computer both choose a champion. The choices include "Bear", "Ninja" or "Cowboy."
Bear eats Ninja. Cowboy shoots Bear. Ninja defeats Cowboy.
Winning adds one point to your score, while losing subtracts one point from your score.
A draw has no effect on your score.  
    """)
    
while player == False:
    # Get player input
    player = input("CHOOSE YOUR FIGHTER: Bear, Ninja, or Cowboy? > ")
    # Generate computer role
    computer = roles[randint(0,2)]
    # Check for valid input
    while player.lower() not in roles:
        player = input("Invalid input.  Please select from Bear, Ninja, or Cowboy. > ")
    print(f"Computer chose > {computer}")
    print("")
    # Compare computer and player roles
    if computer == player:
      print("DRAW!")
      print("")
    elif computer == "cowboy":
      if player.lower() == "bear":
        print("You lose!", computer.capitalize(), "shoots", player.capitalize())
        print("")
        score -= 1
      else: # Computer is cowboy, player is ninja
        print("You win!", player.capitalize(), "defeats", computer.capitalize())
        print("")
        score += 1
    elif computer == "bear":
      if player.lower() == "cowboy":
        print("You win!", player.capitalize(), "shoots", computer.capitalize())
        print("")
        score += 1
      else: # computer is bear, player is ninja
        print("You lose!", computer.capitalize(), "eats", player.capitalize())
        print("")
        score -= 1
    elif computer == "ninja":
      if player.lower() == "cowboy":
        print("You lose!", computer.capitalize(), "defeats", player.capitalize())
        print("")
        score -= 1
      else: # computer is ninja, player is bear
        print("You win!", player.capitalize(), "eats", computer.capitalize())
        print("")
        score += 1
    # Check for replay
    play_again = input(f"Your current score is: {score}. Would you like to play again? (yes/no) > ")
    if play_again.lower() == 'yes':
        print("")
        player = False
        computer = roles[randint(0,2)]
    else:
        print("Goodbye!")
        print("")
        break
