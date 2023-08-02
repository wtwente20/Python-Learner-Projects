import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

print("Lets play a game")
print()

while True:
    playerInput = input("Player (rock, paper, or scissors) > ").lower()
    print()
    if playerInput not in ["rock", "paper", "scissors"]:
        print("Invalid selection! Please choose from: rock, paper, or scissors.")
    else:
        computerInput = get_computer_choice()
        print("Computer chose: " + computerInput)
        print()

        if playerInput == "rock":
            if computerInput == "rock":
                print("Draw!")
            elif computerInput == "scissors":
                print("Player wins!")
            elif computerInput == "paper":
                print("Computer wins!")
        elif playerInput == "paper":
            if computerInput == "rock":
                print("Player wins!")
            elif computerInput == "scissors":
                print("Computer wins!")
            elif computerInput == "paper":
                print("Draw!")
        elif playerInput == "scissors":
            if computerInput == "rock":
                print("Computer wins!")
            elif computerInput == "paper":
                print("Player wins!")
            elif computerInput == "scissors":
                print("Draw!")
        break
