import random

def nextBestMove():
    print("Are you X's or O's")
    xoro = str(input())
    if xoro == str('X'):
        print('Has anyone gone yet?')
        startNewGame = input()
        if startNewGame == str('no'):
            newGameX()
    
    else:
        print('Has anyone gone yet?')
        startNewGame = input()
        if startNewGame == str('no'):
            newGameO()




def newGameX():
        print("Who's going first? X or O or do you want me to decide?")
        goingFirst = str(input())
        if goingFirst == str('X'):
            newGameXfirst()
        elif goingFirst == str('O'):
            newGameXsecond()
        else:
            whosFirts = random.randint(1,2)
            if whosFirts == 1:
                print ('X goes first')
                newGameXfirst()
            else:
                print('O goes first')
                newGameXsecond()

def newGameO():
        print("Who's going first? X or O or do you want me to decide?")
        goingFirst = str(input())
        if goingFirst == str('O'):
            newGameOfirst()
        elif goingFirst == str('X'):
            newGameOsecond()
        else:
            whosFirts = random.randint(1,2)
            if whosFirts == 1:
                print ('X goes first')
                newGameOsecond()
            else:
                print('O goes first')
                newGameOfirst()

def newGameXfirst():
    print('you win!')

def newGameXsecond():
    print('you lose!')

def newGameOfirst():
    print('you win!')

def newGameOsecond():
    print('you lose!')


nextBestMove()
