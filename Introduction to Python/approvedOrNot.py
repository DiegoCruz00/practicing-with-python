def main():
   printIntroduction()
   getInputData()
   calculateStudentStatus()
   getFinalMessage()
   printFinalMessage()

def printIntroduction():
   print("\n # Approved or not? #")


amountOfMissingDays, grade1, grade2, grade3 = 0, 0, 0, 0

def getInputData():
   global amountOfMissingDays, grade1, grade2, grade3

   amountOfMissingDays = int(input(" > Missing days: "))
   grade1 = float(input(" > Grade 1: "))
   grade2 = float(input(" > Grade 2: "))
   grade3 = float(input(" > Grade 3: "))


average = 0
failedForMissingDays, approved = False, False
failedForLowGrades, finalTestIsRequired = False, False

def calculateStudentStatus():
   global average
   average = (grade1 + grade2 + grade3) / 3

   global failedForMissingDays, approved, failedForLowGrades, finalTestIsRequired

   failedForMissingDays = amountOfMissingDays >= 8
   approved = average >= 7 and not failedForMissingDays
   failedForLowGrades = average < 4 and not failedForMissingDays
   finalTestIsRequired = 4 <= average < 7 and not failedForMissingDays

   if finalTestIsRequired and not failedForMissingDays:
      getGradeOnFinalTest()


passedTheFinalTest = False
gradeOnFinalTest = 0

def getGradeOnFinalTest():
   global gradeOnFinalTest, passedTheFinalTest, average

   gradeOnFinalTest = float(input(" > Grade on final test: "))
   newAverage = 0.4 * gradeOnFinalTest + 0.6 * average
   passedTheFinalTest = newAverage >= 5

   average = newAverage


message = "\n"

def getFinalMessage():
   global message

   if failedForMissingDays:
      message += "Sinto muito. Você foi reprovado por faltas."

   else:
      if finalTestIsRequired:
         if passedTheFinalTest:
            message += "Parabéns. Você foi aprovado na final."
         else:
            message += "Sinto muito. Você foi reprovado na final."
      else:
         if approved:
            message += "Parabéns. Você foi aprovado por média."

         elif failedForLowGrades:
            message += "Sinto muito. Você foi reprovado por média."


def printFinalMessage():
   print(message)
   print(" > Média final = {:.1f}".format(average))

main()
