class Student:
   """Parameters: name, creditHours, qualityPoints"""

   def __init__(self, name, creditHours, qualityPoints):
      self.name = name
      self.creditHours = float(creditHours)
      self.qualityPoints = float(qualityPoints)

   def getName(self):
      return self.name

   def getCreditHours(self):
      return self.creditHours

   def getQualityPoints(self):
      return self.qualityPoints

   def getGPA(self):
      return self.qualityPoints / self.creditHours
