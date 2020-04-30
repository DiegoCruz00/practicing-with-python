from Dice import Dice
from PokerInterface import PokerInterface

class PokerApp:
   def __init__(self):
      self.dice = Dice()
      self.money = 100
      self.interface = PokerInterface(self.money)

   def run(self):
      while self.money >= 10 and self.interface.wantToPlay():
         self.playRound()

      self.interface.close()

   def playRound(self):
      self.money -= 10

      self.doRolls()

      result, score = self.dice.getPayoff()
      self.money += score

      self.interface.updateMoney(self.money)
      self.interface.showResults(result, score)

   def doRolls(self):
      self.dice.rollAll()
      roll = 1

      self.interface.updateDice(self.dice.getValues())

      while True:
         if roll < 3:
            diceToRoll = self.interface.chooseDice()

            if diceToRoll == []: break
            else:
               self.dice.roll(diceToRoll)
               self.interface.updateDice(self.dice.getValues())

               roll += 1

         else: break
