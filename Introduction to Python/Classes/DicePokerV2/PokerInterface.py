from os import system

class PokerInterface:
   def __init__(self, money):
      self.money = money
      self.diceValues = []
      self.bottomMessage = ""

   def updateMoney(self, money):
      self.money = money
      self.updateScreen()

   def updateDiceValues(self, diceValues):
      self.diceValues = diceValues
      self.updateScreen()

   def askIfWantToPlay(self):
      while True:
         self.updateScreen()
         answer = input("\n  Do you want to try your luck (y / n) ? ")

         if answer:
            if answer[0].lower() == "y":
               return True
            elif answer[0].lower() == "n":
               return False

   def chooseDice(self):
      self.updateScreen()

      inputValues = input("\n  Which dice do you want roll again? ")
      inputValues = inputValues.replace(" ", "")

      diceToRoll = []

      if inputValues:
         for value in inputValues:
            diceToRoll.append(int(value) - 1)

      return diceToRoll

   def showResults(self, result, score):
      self.bottomMessage = " > You got '{}' and won ${}!\n".format(result, score)
      self.updateScreen()

   def messageTicketOutlay(self):
      self.bottomMessage = " > A game has started for $10\n"
      self.updateScreen()

   def close(self, numberOfGames):
      if self.money < 10:
         print("\n You don't have enough money to play again :(")
         print("\n Bye!")

      else:
         print("\nThanks for playing!")

      print("(Games played: {})".format(numberOfGames))

   def updateScreen(self):
      system("cls")

      displayData = "\n" + "_" * 16 + " DICE POKER! " + "_" * 16 + "\n\n"
      displayData += "  Balance: $ {}\n\n".format(self.money)

      if self.diceValues != []:
         displayData += " " * 12 + "|"

         for die in self.diceValues:
            displayData += " {} |".format(die)

         displayData += "\n\n"

      displayData += self.bottomMessage

      print(displayData, end=("_" * 45 + "\n"))
