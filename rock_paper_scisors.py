#This program is a game of rock pape scissors
import sys
import random

print('ROCK PAPER SCISSORS')
wins = 0
losses = 0              #setting values to 0
ties = 0

while True:
    print(str(wins) + ' Wins ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')       #displaying the wins, losses and ties
    print('Enter your move (r)ock (p)aper (s)cissor or (q)uit')                         #promt user to input options
    move = input()


    #choices
    if (move == 'r'):
        print('ROCK versus...')
    elif (move == 'p'):
        print('PAPER versus...')
    elif (move == 's'):
        print('SCISSORS versus...')
    elif (move == 'q'):
        print('Thanks for playing')
        sys.exit()
    else:
        print('Wrong Input')

    #computer generate random integers from 1 to 3
    counterMove = random.randint(1, 3)

    if(counterMove == 1):
        counterMove = 'r'
        print('ROCK')
    elif(counterMove == 2):
        counterMove = 'p'
        print('PAPER')
    elif(counterMove == 3):
        counterMove = 's'
        print('SCISSORS')

    #evaluate moves
    if(counterMove == move):
        print('It is a tie!')
        ties = ties + 1
        losses = losses + 1
    elif(counterMove == 'r' and move == 'p'):
        print('You win!')
        wins = wins + 1
    elif(counterMove == 'p' and move == 'r'):
        print('I win!')
        losses = losses + 1
    elif(counterMove == 'r' and move == 's'):
        print('I win!')
        losses = losses + 1
    elif(counterMove == 's' and move == 'r'):
        print('You win!')
        wins = wins + 1
    elif(counterMove == 'p' and move == 's'):
        print('You win!')
        wins = wins + 1
    elif(counterMove == 's' and move == 'p'):
        print('I win!')
        losses = losses + 1