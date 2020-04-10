from random import random

def main():
   printIntro()
   probA, probB, numberOfGames = getInputs()
   winsA, winsB = simNGames(numberOfGames, probA, probB)
   printSummary(winsA, winsB)

def printIntro():
   print("This program simulates a game of racquetball between two")
   print("player called 'A' and 'B'. The ability of each player is")
   print("indicated by the probability (a number between 0 and 1) that")
   print("the player wins the point when serving. Player A always has")
   print("the first serve.")

def getInputs():
   a = float(input("> What is the prob. player A wins a serve? "))
   b = float(input("> What is the prob. player B wins a serve? "))
   n = int(input("> How many games to simulate? "))

   return a, b, n

def simNGames(numberOfGames, probA, probB):
   winsA = 0
   winsB = 0

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

         serving = "B"
      else:
         if random() < probB:
            scoreB += 1

         serving = "A"

   return scoreA, scoreB

def gameOver(scoreA, scoreB):
   return scoreA == 15 or scoreB == 15 or (scoreA == 7 and scoreB == 0) or (scoreB == 7 and scoreA == 0)

def printSummary(winsA, winsB):
   numberOfGames = winsA + winsB

   print("Games simulated: {}".format(numberOfGames))
   print("Wins for A: {} ({:.1%})".format(winsA, winsA / numberOfGames))
   print("Wins for B: {} ({:.1%})".format(winsB, winsB / numberOfGames))

main()
