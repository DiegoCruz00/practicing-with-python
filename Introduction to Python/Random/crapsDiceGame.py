from random import randrange

def main():
   printIntro()
   numberOfGames = getInput()
   wins = simulateGames(numberOfGames)
   printSummary(wins, numberOfGames)


def printIntro():
   print("\n# This program simulates a number or games of the Craps game:")
   print(" " * 7 + "(Craps is a dice game played in many cassinos)")


def getInput():
   n = int(input(" > Number of games to simulate: "))
   return n


def simulateGames(numberOfGames):
   wins = 0

   for i in range(numberOfGames):
      win = simulateOneGame()

      if win:
         wins += 1

   return wins


def simulateOneGame():
   initialRoll = rollDices()

   if initialRoll == 2 or initialRoll == 3 or initialRoll == 12:
      win = False
   elif initialRoll == 7 or initialRoll == 11:
      win = True
   else:
      while True:
         newRoll = rollDices()

         if newRoll == initialRoll:
            win = True
            break
         elif newRoll == 7:
            win = False
            break

   return win


def rollDices():
   return randrange(1, 7) + randrange(1, 7)


def printSummary(wins, numberOfGames):
   print("\n Number of games simulated: {}".format(numberOfGames))
   print(" Wins: {} ({:.1%})".format(wins, wins / numberOfGames))


main()
