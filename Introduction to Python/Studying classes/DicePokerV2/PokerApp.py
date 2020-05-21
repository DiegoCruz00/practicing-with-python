from Dice import Dice
from PokerInterface import PokerInterface

class PokerApp:
   def __init__(self):
      self.money = 100
      self.numberOfGames = 0
      self.dice = Dice()
      self.interface = PokerInterface(self.money)

   def run(self):
      self.interface.updateScreen()

      while self.money >= 10 and self.interface.askIfWantToPlay():
         self.numberOfGames += 1

         self.doRoll()

         result, score = self.dice.getCategory()

         self.money += score
         self.interface.updateMoney(self.money)
         self.interface.showResults(result, score)

      self.verifyLeaderboardPosition()
      self.interface.close(self.numberOfGames)

   def doRoll(self):
      self.money -= 10
      self.interface.updateMoney(self.money)
      self.interface.messageTicketOutlay()

      rolls = 1

      self.dice.rollAll()
      diceValues = self.dice.getValues()
      self.interface.updateDiceValues(diceValues)

      while rolls < 3:
         rolls += 1

         diceToRoll = self.interface.chooseDice()

         if diceToRoll == []:
            break
         else:
            self.dice.roll(diceToRoll)
            diceValues = self.dice.getValues()
            self.interface.updateDiceValues(diceValues)

   def verifyLeaderboardPosition(self):
      path = "E:/Diego/ComputerScience/Programming/Training Projects/Python/Introduction to Python/Classes/DicePokerV2/highestScores.txt"
      highestScoreFile = open(path, "r")

      self.highestScores = self.getHighestScoresFrom(highestScoreFile)

      for i in range(10):
         if self.money > self.highestScores[i][1]:
            self.username = self.askForUsername()
            self.updateLeaderboardList()
            break

      self.highestScores.sort(key=self._userScore, reverse=True)
      self.reduceLeaderboardListToTen()

      highestScoreFile.close()
      highestScoreFile = open(path, "w")

      for userData in self.highestScores:
         print("{}, {}".format(userData[0], userData[1]), file=highestScoreFile)

      highestScoreFile.close()

   def getHighestScoresFrom(self, file):
      highestScores = []
      for userData in file:
         username, score = userData.split(", ")
         highestScores.append([username, int(score)])

      return highestScores

   def askForUsername(self):
      return input("\n You've got a new record! Enter your username: ")

   def updateLeaderboardList(self):
      userFound = False

      for i in range(10):
         if self.username == self.highestScores[i][0]:
            userFound = True

            if self.money > self.highestScores[i][1]:
               self.highestScores[i][1] = self.money

            break

      if not userFound:
         self.highestScores.append([self.username, self.money])

   def _userScore(self, userData):
      return userData[1]

   def reduceLeaderboardListToTen(self):
      for i in range(len(self.highestScores) - 10):
         self.highestScores.pop()

