def main():
   printIntroduction()
   getInputData()
   calculateBill()
   printResults()

def printIntroduction():
   print("\n >>> Babysitter Bill Calculator <<<")

interval = []

def getInputData():
   global interval

   interval.append(input(" > Starting time: "))
   interval.append(input("   > Ending time: "))

   for i in range(2):
      time, daySection = interval[i].split()

      time = time.split(":")

      for j in range(2):
         time[j] = int(time[j])

      if daySection.upper() == "PM" and time[0] != 12:
         time[0] = time[0] + 12

      if daySection.upper() == "AM" and time[0] == 12:
         time[0] = 0

      interval[i] = time

bill, workedHours, workedMinutes = 0, 0, 0

def calculateBill():
   startingHour = interval[0][0]
   startingMinute = interval[0][1]
   endingHour = interval[1][0]
   endingMinute = interval[1][1]

   global workedHours, workedMinutes

   if endingMinute < startingMinute:
      workedMinutes = 60 - startingMinute + endingMinute
   elif endingMinute > startingMinute:
      workedMinutes = endingMinute - startingMinute
   else:
      workedMinutes = 0

   startingMinute += workedMinutes

   if startingMinute >= 60:
      startingHour += startingMinute // 60

   if endingHour < startingHour:
      workedHours = 24 - startingHour + endingHour
   elif endingHour > startingHour:
      workedHours = endingHour - startingHour
   else:
      workedHours = 0

   global bill
   bill = (workedHours + (workedMinutes / 60)) * 2.5

def printResults():
   print("\n     >>> Total bill: ${:.2f}".format(bill))
   print("           (worked hours: {}:{:0>2})".format(workedHours, workedMinutes))

main()
