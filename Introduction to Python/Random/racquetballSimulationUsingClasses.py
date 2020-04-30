from random import random

class SimulationStats:
   def __init__(self):
      self.winsA = 0
      self.winsB = 0
      self.shutoutsA = 0
      self.shutoutsB = 0

   def update(self, game):
      scoreA, scoreB = game.getScores()

      if scoreA > scoreB:
         self.winsA += 1
         if scoreA == 7:
            self.shutoutsA += 1

      elif scoreB > scoreA:
         self.winsB += 1
         if scoreB == 7:
            self.shutoutsB += 1

   def printReport(self):
      print("\nSummary of {} games:\n".format(self.winsA + self.winsB))

      self._printHeading()
      self._printLine("Player A")
      self._printLine("Player B")

   def _printHeading(self):
      print(" " * 13 + "Wins (% total)   Shutouts (% wins)")
      print("-" * 49)

   def _printLine(self, label):
      if label == "Player A":
         wins = self.winsA
         shutouts = self.shutoutsA
      else:
         wins = self.winsB
         shutouts = self.shutoutsB

      numberOfGames = self.winsA + self.winsB

      print("{}      ".format(label), end="")
      print("{:^6} {:^7.1%}".format(wins, wins / numberOfGames), end="")

      if wins > 0:
         print("    {:^6} {:^5.1%}".format(shutouts, shutouts / wins))
      else:
         print("       -     - %")

class Player:
   def __init__(self, prob):
      self.prob = prob
      self.score = 0

   def getScore(self):
      return self.score

   def wonServe(self):
      return random() < self.prob

   def incrementScore(self):
      self.score += 1

class RacquetballGame:
   def __init__(self, probA, probB):
      self.playerA = Player(probA)
      self.playerB = Player(probB)
      self.server = self.playerA

   def play(self):
      while not self._gameOver():
         if self.server.wonServe():
            self.server.incrementScore()
         else:
            self._changeServer()

   def getScores(self):
      return self.playerA.getScore(), self.playerB.getScore()

   def _gameOver(self):
      scoreA, scoreB = self.getScores()

      return scoreA == 15 or scoreB == 15 \
          or (scoreA == 7 and scoreB == 0) or (scoreB == 7 and scoreA == 0)

   def _changeServer(self):
      if self.server == self.playerA:
         self.server = self.playerB
      else:
         self.server = self.playerA


def main():
   printIntro()

   probA, probB, numberOfGames = getInputs()
   stats = SimulationStats()

   for i in range(numberOfGames):
      game = RacquetballGame(probA, probB)
      game.play()

      stats.update(game)

   stats.printReport()


def printIntro():
   print("This program simulates a game of racquetball between two")
   print("player called 'A' and 'B'. The ability of each player is")
   print("indicated by the probability (a number between 0 and 1) that")
   print("the player wins the point when serving. Player A always has")
   print("the first serve.")

def getInputs():
   a = float(input(" > Probability of Team A to win when serving: "))
   b = float(input(" > Probability of Team B to win when serving: "))
   n = int(input(" > Number of games to be simulated: "))

   return a, b, n

main()
