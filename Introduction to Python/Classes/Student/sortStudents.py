from tkinter.filedialog import askopenfilename, asksaveasfilename
from Student import Student

def main():
   inputFile = open(askopenfilename(), "r")

   listOfStudents = readStudents(inputFile)

   mode = askSortingMode()
   sortedStudents = sortStudents(listOfStudents, mode)

   outputFile = open(asksaveasfilename(), "w")
   printSortedStudentsAtFile(sortedStudents, outputFile)

   print("\n Students sorted successfully!")

   inputFile.close()
   outputFile.close()


def readStudents(file):
   students = []

   for line in file:
      name, creditsHours, qualityPoints = line.split(", ")

      newStudent = Student(name, creditsHours, qualityPoints)
      students.append(newStudent)

   return students


def askSortingMode():
   while True:
      printInputGuide()

      mode = input("\n   > ")

      if isValidMode(mode):
         return mode.split(" -")
      else:
         print("\nERROR: invalid sorting method\n")


def isValidMode(modeString):
   try:
      modeString = modeString.split(" -")

      key = modeString[0]
      reverse = modeString[1]

      if key not in ["gpa", "name", "quality-point", "credit"]:
         return False

      if reverse not in ["a", "d"]:
         return False

      return True

   except:
      return False


def printInputGuide():
   print("\n> Sorting method:")
   print("    'gpa' for sorting students by GPA")
   print("    'name' for sorting students by name")
   print("    'quality-point' for sorting students by quality points")
   print("    'credit' for sorting students by credits\n")
   print("    ' -a' sort ascending")
   print("    ' -d' sort descending")


def sortStudents(listOfStudents, mode):
   key = mode[0]
   reverse = mode[1]

   reverseBool = False

   if reverse == "a":
      reverseBool == False
   elif reverse == "d":
      reverseBool = True

   if key == "gpa":
      listOfStudents.sort(key=Student.getGPA, reverse=reverseBool)
   elif key == "name":
      listOfStudents.sort(key=Student.getName, reverse=reverseBool)
   elif key == "quality-point":
      listOfStudents.sort(key=Student.getQualityPoints, reverse=reverseBool)
   elif key == "credit":
      listOfStudents.sort(key=Student.getCreditHours, reverse=reverseBool)

   return listOfStudents


def printSortedStudentsAtFile(listOfStudents, outputFile):
   for student in listOfStudents:
      print("{}, {}, {}".format(
         student.getName(),
         student.getCreditHours(),
         student.getQualityPoints()),

         file=outputFile)


main()
