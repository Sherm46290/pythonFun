# Name: Richard Sherman
# Date: 7/22/19
# Filename: game.py
# Description: Rock, Paper, Scissors, Lizard, Spock game

import random



# welcome and name input
print("Welcome to the Rock-Paper-Scissors-Lizard-Spock Game")
name = input("Please enter your name: ")
name = name.title()

# game rules
print("Welcome " + name + ", here are the rules of the game:")
print("********************************")
print("Rule #1: scissors cuts paper")
print("Rule #2: paper covers rock")
print("Rule #3: rock crushes lizard")
print("Rule #4: lizard poisons spock")
print("Rule #5: spock smashes scissors")
print("Rule #6: scissors decapitates lizard")
print("Rule #7: lizard eats paper")
print("Rule #8: paper disproves spock")
print("Rule #9: spock vaporizes rock")
print("Rule #10: rock crushes scissors")
print("********************************")

print()
print()

num_games = int(input("How many games would you like to play? "))


def game():
    # loop for number of games to play
    for i in range(num_games):
        player = input("Enter rock, paper, scissors, lizard or spock:")
        computer = random.randint(1, 5)
        if computer == 1:
            print("CPU chooses rock")
        elif computer == 2:
            print("CPU chooses paper")
        elif computer == 3:
            print("CPU chooses scissors")
        elif computer == 4:
            print("CPU chooses lizard")
        elif computer == 5:
            print("CPU chooses spock")
# tie scennarios
        if computer == 1 and player == ("rock"):
            print("You tied!")
            print()
        elif computer == 2 and player == ("paper"):
            print("You tied!")
            print()
        elif computer == 3 and player == ("scissors"):
            print("You tied!")
            print()
        elif computer == 4 and player == ("lizard"):
            print("You tied!")
            print()
        elif computer == 5 and player == ("spock"):
            print("You tied!")
            print()
        else:
# CPU and player win conditions
            if computer == 1 and player == ("scissors") or computer == 1 and player == ("lizard"):
                output = "CPU wins!"
            elif computer == 2 and player == ("rock") or computer == 2 and player == ("spock"):
                output = "CPU wins!"
            elif computer == 3 and player == ("paper") or computer == 3 and player == ("lizard"):
                output = "CPU wins!"
            elif computer == 4 and player == ("spock") or computer == 4 and player == ("paper"):
                output = "CPU wins!"
            elif computer == 5 and player == ("scissors") or computer == 5 and player == ("rock"):
                output = "CPU wins!"
            else:
                output = name + " wins!"
            print(output)
            print()
game()

if num_games >= num_games:
    print("Thanks for playing!")





