from random import uniform


def main():
   printIntro()
   numOfThrows = getInput()
   wins = simulateThrows(numOfThrows)
   printSummary(wins, numOfThrows)


def printIntro():
   print("\n# This program simulates a game of darts targeted at a round dartboard")
   print(" inside a square cabinet:")


def getInput():
   num = int(input(" > Number of darts to be thrown: "))
   return num


def simulateThrows(numOfThrows):
   wins = 0

   for i in range(numOfThrows):
      win = simulateOneThrow()
      if win:
         wins += 1

   return wins


def simulateOneThrow():
   dartboardRadius = 2

   x = uniform(-dartboardRadius, dartboardRadius)
   y = uniform(-dartboardRadius, dartboardRadius)

   distanceToCenter = (x**2 + y**2) ** 0.5

   if distanceToCenter <= dartboardRadius:
      win = True
   else:
      win = False

   return win


def printSummary(wins, numOfThrows):
   print("  >> Number of games simulated: {}".format(numOfThrows))
   print("  >> Wins: {} ({:.1%})".format(wins, wins / numOfThrows))


main()
