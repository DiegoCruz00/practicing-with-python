class Attendee:
   def __init__(self, data):
      self.name = data["name"]
      self.company = data["company"]
      self.state = data["state"]
      self.email = data["email"]

   def getName(self):
      return self.name

   def getState(self):
      return self.state

   def getEmail(self):
      return self.email

   def getData(self):
      return {
         "name": self.name,
         "company": self.company,
         "state": self.state,
         "email": self.email
      }
