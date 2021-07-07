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

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def newGameXfirst():
    print('Put an X in the bottom left corner')
    theBoard['low-L'] = 'X'

def newGameXsecond():
    print('you lose!')

def newGameOfirst():
    print('Put an O in the bottom left corner')
    theBoard['low-L'] = 'O'

def newGameOsecond():
    print('you lose!')


nextBestMove()



def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)