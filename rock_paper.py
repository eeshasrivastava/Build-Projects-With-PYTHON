# Creates a rock, paper, scissors game where the user
# plays against the computer.

import random               # Imports the random library.

# Creates a list of choices for the user and the computer.
choices = ["rock", "paper", "scissors"]

# Prints the rules of the game.
print("Rock crushes scissors. Scissors cut paper. Paper covers rock.")

# Asks the player what their choice is or if they want to quit the game.
player = input("Do you want to be rock, paper or scissors (or quit)? ")

# Creates a while loop to compare choices and choose a winner.
while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("You chose " +player+ ", and the computer chose " +computer+ ".")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("I think there was some sort of error...")
    print()     # Skips a line.

    # Asks the player what their choice is or if they want to quit the game.
    player = input("Do you want to be rock, paper or scissors (or quit)? ")
