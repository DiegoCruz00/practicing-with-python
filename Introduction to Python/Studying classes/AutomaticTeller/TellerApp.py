from User import User
from os import path, system

class TellerApp:
   def __init__(self):
      self.root = path.dirname(path.abspath(__file__))

   def run(self):
      dataFile = open("{}/data.txt".format(self.root), "r")

      self.users = []
      for userData in dataFile:
         self.users.append(User(eval(userData)))

      dataFile.close()

      self.askForLogIn()

   def askForLogIn(self):
      system("cls")
      print("\n   AUTOMATIC TELLER MACHINE")

      userID = input("\n ID: ")
      userPassword = input(" Password: ")

      if self.loginSuccessful(userID, userPassword):
         self.enableAccess()
      else:
         print("\n ID and/or password are incorrect. \n")
         input(" <press enter to try again>\n")

         self.askForLogIn()

   def loginSuccessful(self, userID, userPassword):
      for user in self.users:
         if user.login(userID, userPassword):
            self.currentUser = user
            return True

      return False

   def enableAccess(self):
      while True:
         system("cls")

         print("\n Welcome, {}!\n".format(self.currentUser.getName()))

         answer = self.askForAnAction()

         if answer == "l":
            self.logOut()
            break
         else:
            if answer == "c":
               self.checkBalances()
            elif answer == "w":
               self.withdrawCash()
            elif answer == "t":
               self.transferMoney()

   def askForAnAction(self):
      print("  ( c ) - Check balances")
      print("  ( w ) - Withdraw cash")
      print("  ( t ) - Transfer money")
      print("  ( l ) - Log out")

      return input("\n").lower()

   def logOut(self):
      self.currentUser = None
      self.askForLogIn()

   def checkBalances(self):
      system("cls")

      print("\nCHECK BALANCES:")
      print("\n > Checking account balance: $ {:.2f}"
         .format(self.currentUser.getCheckingBalance()))
      print(" > Savings account balance: $ {:.2f}"
         .format(self.currentUser.getSavingsBalance()))

      input("\n <press enter to return to title>\n")

   def withdrawCash(self):
      self.account = self.askAccountFromWhichTo("w")
      cashToWithdraw = self.askCashTo("w")

      status = self.currentUser.withdraw(self.account.lower(), cashToWithdraw)

      if status == "OK":
         self.saveToDatabank()
         print("\nWithdraw complete! ")
      elif status == "Not enough money":
         print("\nYou do not have this amount in your savings account!")

      input("\n <press enter to return to title>\n")

   def transferMoney(self):
      self.account = self.askAccountFromWhichTo("t")
      cashToTransfer = self.askCashTo("t")

      status = self.currentUser.transfer(self.account.lower(), cashToTransfer)

      if status == "OK":
         self.saveToDatabank()
         print("\n Trafering complete! ")
      elif status == "Not enough money":
         print("\n You do not have enough in this account to transfer!")

      input("\n <press any key to return to title>")

   def askAccountFromWhichTo(self, action):
      while True:
         system("cls")

         if action == "w":
            print("\nWITHDRAW CASH:")
            account = input(" > Account (c - checking | s - savings): ")
         elif action == "t":
            print("\nTRANSFER MONEY:")
            account = input(" > Source account (c - checking | s - savings): ")

         if account.lower() == "c" or account.lower() == "s":
            return account
         else:
            print("\n Invalid entry!")
            input("\n <press enter to try again>\n")

   def askCashTo(self, action):
      while True:
         if action == "w":
            try:
               return float(input(" > Amount to withdraw: "))
            except:
               print("\n Invalid entry! Please be sure to use only numbers and dots!")
               input("\n <press enter to try again>")

               system("cls")
               print("\nWITHDRAW CASH:")
               print(" > Account (c - checking | s - savings): {}".format(self.account))

         elif action == "t":
            try:
               return float(input(" > Amount to transfer: "))
            except:
               print("\nInvalid entry! Please be sure to use only numbers and dots!")
               input("\n <press enter to try again>\n")

               system("cls")
               print("\nTRANSFER MONEY:")
               print(" > Source account (c - checking | s - savings): {}".format(self.account))

   def saveToDatabank(self):
      dataFile = open("{}/data.txt".format(self.root), "w")

      for user in self.users:
         print(user.getAllData(), file=dataFile)

      dataFile.close()
