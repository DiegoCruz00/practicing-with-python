from random import random

def main():
   printIntro()
   probA, probB, numberOfGames = getInputs()
   winsA, winsB = simGames(probA, probB, numberOfGames)
   printSummary(winsA, winsB)

def printIntro():
   print("\nThis program simulates a number of volleyball matches")

def getInputs():
   a = float(input(" > Team A's probability to win a serve: "))
   b = float(input(" > Team B's probability to win a serve: "))
   n = int(input(" > Number of games to simulate: "))

   return a, b, n

def simGames(probA, probB, numberOfGames):
   winsA, winsB = 0, 0

   for i in range(numberOfGames):
      scoreA, scoreB = simOneGame(probA, probB)

      if scoreA > scoreB:
         winsA += 1
      else:
         winsB += 1

   return winsA, winsB

def simOneGame(probA, probB):
   scoreA, scoreB = 0, 0
   serving = "A"

   while not gameOver(scoreA, scoreB):
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

def gameOver(scoreA, scoreB):
   return (abs(scoreA - scoreB) >= 2) and (scoreA >= 15 or scoreB >= 15)

def printSummary(winsA, winsB):
   numberOfGames = winsA + winsB
   print("Number of games simulated: {}".format(numberOfGames))
   print("Wins for A: {} ({:.1%})".format(winsA, winsA / numberOfGames))
   print("Wins for B: {} ({:.1%})".format(winsB, winsB / numberOfGames))

main()
