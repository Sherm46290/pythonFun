import random
import ticTacModules

def nextBestMove():
    print("Are you X's or O's")
    xoro = str.lower(input())
    if xoro == str('x'):
        print('Has anyone gone yet?')
        startNewGame = str.lower(input())
        if startNewGame == str('no'):
            newGameX()
    
    else:
        print('Has anyone gone yet?')
        startNewGame = str.lower(input())
        if startNewGame == str('no'):
            newGameO()




def newGameX():
        print("Who's going first? X or O or do you want me to decide?")
        goingFirst = str.lower(input())
        if goingFirst == str('x'):
            newGameXfirst()
        elif goingFirst == str('o'):
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
        goingFirst = str.lower(input())
        if goingFirst == str('o'):
            newGameOfirst()
        elif goingFirst == str('x'):
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
theOptionsBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


theOptionsBoard['top-L'] = '1'
theOptionsBoard['top-M'] = '2'
theOptionsBoard['top-R'] = '3'
theOptionsBoard['mid-L'] = '4'
theOptionsBoard['mid-M'] = '5'
theOptionsBoard['mid-R'] = '6'
theOptionsBoard['low-L'] = '7'
theOptionsBoard['low-M'] = '8'
theOptionsBoard['low-R'] = '9'


def newGameXfirst():
    print('Put an X in the bottom left corner')
    theBoard['low-L'] = 'X'
    theOptionsBoard['low-L'] = 'X'
    ticTacModules.printBoard(theBoard)
    print('Where did they go? Please pick the spot from 1 to 9.')
    whereTheyWent = str(input())
    if ['2', '4', '5', '6', '8'] in whereTheyWent:
        theBoard['mid-M'] = 'O'
        theOptionsBoard['mid-M'] = 'O'
        print('Put an X in spot 3')
        theBoard['top-R'] = 'X'
        theOptionsBoard['top-R'] = 'X'

def newGameXsecond():
    print('you lose!')

def newGameOfirst():
    print('Put an O in the bottom left corner')
    theBoard['low-L'] = 'O'
    theOptionsBoard['low-L'] = 'O'
    ticTacModules.printBoard(theBoard)
    print('Where did they go? Please pick the spot from 1 to 9.')
    whereTheyWent = int(input())
    if whereTheyWent == 1:
        theBoard['top-L'] = 'X'
        theOptionsBoard['top-L'] = 'X'
        print('Put an O in spot 3')
        theBoard['top-R'] = 'O'
        theOptionsBoard['top-R'] = 'O'
    if whereTheyWent == 2:
        theBoard['top-M'] = 'X'
        theOptionsBoard['top-M'] = 'X'
        print('Put an O in spot 3')
        theBoard['top-R'] = 'O'
        theOptionsBoard['top-R'] = 'O'
    if whereTheyWent == 4:
        theBoard['mid-L'] = 'X'
        theOptionsBoard['mid-L'] = 'X'
        print('Put an O in spot 3')
        theBoard['top-R'] = 'O'
        theOptionsBoard['top-R'] = 'O'
    if whereTheyWent == 5:
        theBoard['mid-M'] = 'X'
        theOptionsBoard['mid-M'] = 'X'
        print('Put an O in spot 3')
        theBoard['top-R'] = 'O'
        theOptionsBoard['top-R'] = 'O'
    if whereTheyWent == 6:
        theBoard['mid-R'] = 'X'
        theOptionsBoard['mid-R'] = 'X'
        print('Put an O in spot 3')
        theBoard['top-R'] = 'O'
        theOptionsBoard['top-R'] = 'O'
    if whereTheyWent == 8:
        theBoard['bot-M'] = 'X'
        theOptionsBoard['bot-M'] = 'X'
        print('Put an O in spot 3')
        theBoard['top-R'] = 'O'
        theOptionsBoard['top-R'] = 'O'
    if whereTheyWent == 9:
        theBoard['bot-R'] = 'X'
        theOptionsBoard['bot-R'] = 'X'
        print('Put an O in spot 3')
        theBoard['top-R'] = 'O'
        theOptionsBoard['top-R'] = 'O'

def newGameOsecond():
    print('you lose!')


nextBestMove()



ticTacModules.printOptionsBoard(theOptionsBoard)