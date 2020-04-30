class User:
   def __init__(self, userData):
      self.name = userData["name"]
      self.id = userData["id"]
      self.password = userData["password"]
      self.checkingBalance = userData["checkingBalance"]
      self.savingsBalance = userData["savingsBalance"]

   def login(self, userID, userPassword):
      return userID == self.id and userPassword == self.password

   def getName(self):
      return self.name

   def getCheckingBalance(self):
      return self.checkingBalance

   def getSavingsBalance(self):
      return self.savingsBalance

   def withdraw(self, account, amount):
      if account == "c":
         if self.checkingBalance >= amount:
            self.checkingBalance -= amount
            return "OK"
         else:
            return "Not enough money"

      if account == "s":
         if self.savingsBalance >= amount:
            self.savingsBalance -= amount
            return "OK"
         else:
            return "Not enough money"

   def transfer(self, sourceAccount, amount):
      if sourceAccount == "c":
         if self.checkingBalance >= amount:
            self.checkingBalance -= amount
            self.savingsBalance += amount
            return "OK"
         else:
            return "Not enough money"

      elif sourceAccount == "s":
         if self.savingsBalance >= amount:
            self.savingsBalance -= amount
            self.checkingBalance += amount
            return "OK"
         else:
            return "Not enough money"


   def getAllData(self):
      return {
         'name': self.name,
         'id': self.id,
         'password': self.password,
         'checkingBalance': self.checkingBalance,
         'savingsBalance': self.savingsBalance
      }
