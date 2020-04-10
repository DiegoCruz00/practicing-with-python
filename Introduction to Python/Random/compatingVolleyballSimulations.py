from random import random

def main():
   printIntro()
   probA, probB, numberOfGames = getInputs()

   winsADefault, winsBDefault = simGames("default", probA, probB, numberOfGames)
   winsARally, winsBRally = simGames("rally", probA, probB, numberOfGames)

   printSummary(winsADefault, winsBDefault, winsARally, winsBRally)


def printIntro():
   print("\nThis program simulates a number of volleyball matches")


def getInputs():
   a = float(input(" > Team A's probability to win a serve: "))
   b = float(input(" > Team B's probability to win a serve: "))
   n = int(input(" > Number of games to simulate: "))

   return a, b, n


def simGames(mode, probA, probB, numberOfGames):
   winsA, winsB = 0, 0

   for i in range(numberOfGames):
      if mode == "default":
         scoreA, scoreB = simOneDefaultGame(probA, probB)
      elif mode == "rally":
         scoreA, scoreB = simOneRallyGame(probA, probB)

      if scoreA > scoreB:
         winsA += 1
      else:
         winsB += 1

   return winsA, winsB


def simOneDefaultGame(probA, probB):
   scoreA, scoreB = 0, 0
   serving = "A"

   while not defaultGameOver(scoreA, scoreB):
      if serving == "A":
         if random() < probA:
            scoreA += 1
         else:
            serving = "B"
      else:
         if random() < probB:
            scoreB += 1
         else:
            serving = "A"

   return scoreA, scoreB


def defaultGameOver(scoreA, scoreB):
   return (abs(scoreA - scoreB) >= 2) and (scoreA >= 15 or scoreB >= 15)


def simOneRallyGame(probA, probB):
   scoreA, scoreB = 0, 0
   serving = "A"

   while not rallyGameOver(scoreA, scoreB):
      if serving == "A":
         if random() < probA:
            scoreA += 1
         else:
            scoreB += 1
            serving = "B"
      else:
         if random() < probB:
            scoreB += 1
         else:
            scoreA += 1
            serving = "A"

   return scoreA, scoreB


def rallyGameOver(scoreA, scoreB):
   return (abs(scoreA - scoreB) >= 2) and (scoreA >= 25 or scoreB >= 25)


def printSummary(winsADefault, winsBDefault, winsARally, winsBRally):
   numberOfGames = winsADefault + winsBDefault

   print("\nNumber of games simulated: {}\n".format(numberOfGames))

   print("Default Volleyball Summary: ")
   print(" > Wins for A: {} ({:.1%})".format(winsADefault, winsADefault / numberOfGames))
   print(" > Wins for B: {} ({:.1%})".format(winsBDefault, winsBDefault / numberOfGames))
   print("Rally Volleyball Summary: ")
   print(" > Wins for A: {} ({:.1%})".format(winsARally, winsARally / numberOfGames))
   print(" > Wins for B: {} ({:.1%})".format(winsBRally, winsBRally / numberOfGames))


main()
