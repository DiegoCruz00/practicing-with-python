def main():
   getInputDate()
   verifyDate()

   if status == "OK":
      calculateDayNumber()

   printResutls()


date = ""

def getInputDate():
   global date
   date = input("\n Insert a date (mm/dd/yyyy): ")


status = "OK"

def verifyDate():
   verifyInputCharacters()

   if status == "OK":
      verifyMonthDayYear()

def verifyInputCharacters():
   global status

   for character in date:
      if not(character.isnumeric()) and character != "/":
         status = "invalid date"

   if date.count("/") != 2:
      status = "invalid date"

month, day, year = 0, 0, 0

def verifyMonthDayYear():
   global status, month, day, year

   month, day, year = date.split("/")

   month = int(month)
   day = int(day)
   year = int(year)

   if month > 12 or month < 1 or day < 1:
      status = "invalid date"

   else:
      if month in [1, 3, 5, 7, 8, 10, 12]:
         if day > 31:
            status = "invalid date"
      elif month == 2:
         if isLeapYear():
            if day > 29:
               status = "invalid date"
         else:
            if day > 28:
               status = "invalid date"
      else:
         if day > 30:
            status = "invalid date"


def isLeapYear():
   return year % 4 == 0

dayNumber = 0

def calculateDayNumber():
   global dayNumber

   for i in range(1, month):
      if i in [1, 3, 5, 7, 8, 10, 12]:
         dayNumber += 31
      elif i == 2:
         if isLeapYear():
            dayNumber += 29
         else:
            dayNumber += 28
      else:
         dayNumber += 30

   dayNumber += day

def printResutls():
   if status == "OK":
      print(" > Valid date!")
      print("    (Day {})".format(dayNumber))
   else:
      print(" > Invalid date!")


main()
