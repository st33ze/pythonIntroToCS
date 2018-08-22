# This program simulates racquetball games, between two players A and B.
# First it prompts the user to type probability of winning for both
# players and how many games to simulate. With rand function it
# decides which player serves first (coinflip) and then it simulates a
# game, adding a point to the score depending on which player wins. After,
# it repeats the process, depending on how many games user typed at
# promt. Finally it prints summed up results.

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simulateNGames(probA, probB, n)
    printResults(winsA, winsB)

def printIntro():
    print('This program simulates games of racquetball between two')
    print('players called "A" and "B". The abilities of each player is')
    print('indicated by a probability (a number between 0 and 1) that')
    print('the player wins the point when serving. Decision which player')
    print('serves is made by a coinflip.')

def getInputs():
    # Returns probability values and number of games to simulate
    while(True):
        print()
        a = input('Please enter player A win probability (e.g 0.72): ')
        b = input('Please enter player B win probability (e.g 0.5): ')
        n = input('Please enter number of games to simulate: ')

        # Inputs validation
        try:
            a, b = float(a), float(b)
            n = int(n)
        except:
            print()
            print('Wrong input. Try again')

        if (a > 0 and a < 1) and (b > 0 and b < 1) and n > 0:
            return a, b, n      # Validation passed
        else:
            print()
            print('Wrong input. Try again.')

def simulateNGames(probA, probB, n):
    # Returns wins amount for both players
    # Set counters to 0
    winsA = winsB = 0
    for game in range(n):
        scoreA, scoreB = simulateGame(probA, probB)
        if scoreA == 15:
            winsA += 1
        else:
            winsB += 1

    return winsA, winsB

def simulateGame(probA, probB):
    # Returns score of both players for one game
    scoreA = scoreB = 0

    # Draw which player is serving
    serve = 'A'
    if random() >= 0.5:
        serve = 'B'

    while not gameOver(scoreA, scoreB):
        if serve == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serve = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serve = 'A'

    return scoreA, scoreB

def gameOver(scoreA, scoreB):
    # Returns true if one of the players scored 15 points
    return scoreA == 15 or scoreB == 15

def printResults(a, b):
    print()
    print('Total games simulated: {}.'.format(a + b))
    print('Player A won {0} times, which is {1:0.1%} of total games played.'
          .format(a, a / (a + b)))
    print('Player B won {0} times, which is {1:0.1%} of total games played.'
          .format(b, b / (a + b)))

if __name__ == '__main__':
    main()
