# Name: Richard Sherman
# Date: 8/13/19
# Filename: madlibs.py
# Description: Madlibs console game

import os

def playGame():
    showMenu()
    choice = int(input())
    if choice == 1:
        madlib = makeMadlib()
        printMadlib(madlib)
    else:
        print("Thanks for playing!")

# main menu for introduction to game
def showMenu():
    print("Welcome to the Madlibs Console Game!")
    print("Please make a choice from the menu below.")
    print("1: Make a madlib \n2: Exit \nChoice: ")

# convert user input to filepath
def makeMadlib():
    fileName = input("Please enter a file name(jungle, zoo or school): ")
    if fileName == 'jungle':
        fileName = 'files/jungle.madlib'
    elif fileName == 'school':
        fileName = "files/school.madlib"
    elif fileName == 'zoo':
        fileName = "files/zoo.madlib"
    else:
        print("Sorry, that filename doesn't exist. \nGoodbye")
        exit()

# check if file exists
    if os.path.exists(fileName):
        file = open(fileName, "r")
        lines = file.readlines()
        for i in range(len(lines)):

# get user input for nouns, adjective or verb
            while lines[i].__contains__("<noun>") or lines[i].__contains__("<adjective>") or lines[i].__contains__("<verb>"):
                if "<noun>" in lines[i]:
                    userInput = input("Please type a noun: ")
                    lines[i] = lines[i].replace("<noun>", userInput)
                elif "<adjective>" in lines[i]:
                    userInput = input("Please type a adjective: ")
                    lines[i] = lines[i].replace("<adjective>", userInput)
                elif "<verb>" in lines[i]:
                    userInput = input("Please type a verb: ")
                    lines[i] = lines[i].replace("<verb>", userInput)
        print()
        print()
        return lines


# print madlib with user input
def printMadlib(madlib):
    for i in range(len(madlib)):
        print(madlib[i], end="")
    print()
    print()
    playGame()

# start program
playGame()