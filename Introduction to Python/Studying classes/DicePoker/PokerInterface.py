class PokerInterface:
   def __init__(self, initialMoney):
      self.initialMoney = initialMoney
      self.money = initialMoney
      self.numberOfGames = 0

      self.printIntro()
      print("> You currently have: ${}".format(self.money))


   def printIntro(self):
      print("\nWelcome to Dice Poker!\n")

   def updateMoney(self, money):
      self.money = money
      print("> You currently have: ${}".format(self.money))

   def updateDice(self, diceValues):
      print(" Dice: {}".format(diceValues))

   def wantToPlay(self):
      answer = input("\n   Do you want to try your luck? (y / n) ")

      if answer.lower() == "y":
         self.numberOfGames += 1
         return True

   def chooseDice(self):
      return eval(input(" Enter a list of which dice to roll again: "))

   def updateInterface(self):
      print("> You currently have: ${}".format(self.money))

   def showResults(self, result, score):
      print(" Result of this round: {} (+ ${})".format(result, score))

   def close(self):
      print("\nFinal Summary:")
      print("   > Initial money: $ {}".format(self.initialMoney))
      print("   > Current money: $ {}".format(self.money))
      print("   > Games played: {}".format(self.numberOfGames))
      print("\n Thanks for playing!\n")
