from tkinter.filedialog import askopenfilename
from Student import Student

def main():
   inputFile = openSelectedFile()

   listOfStudents = []
   for line in inputFile:
      listOfStudents.append(makeStudentFromLine(line))

   greatestGPA = getGreatestGPA(listOfStudents)
   bestStudents = getStudentsWithGPA(listOfStudents, greatestGPA)

   printSummary(bestStudents)

   inputFile.close()


def openSelectedFile():
   filePath = askopenfilename()

   return open(filePath, "r")


def makeStudentFromLine(line):
   name, creditHours, qualityPoints = line.split(", ")

   return Student(name, creditHours, qualityPoints)


def getGreatestGPA(listOfStudents):
   greatestGPA = 0

   for student in listOfStudents:
      if student.getGPA() > greatestGPA:
         greatestGPA = student.getGPA()

   return greatestGPA


def getStudentsWithGPA(listOfStudents, gpa):
   filteredStudents = []

   for student in listOfStudents:
      if student.getGPA() == gpa:
         filteredStudents.append(student)

   return filteredStudents


def printSummary(bestStudents):
   print("\n The best ", end="")

   if len(bestStudents) == 1:
      print("student is:")
   elif len(bestStudents) > 1:
      print("students are:")

   for bestStudent in bestStudents:
      print("\n Name: {}".format(bestStudent.getName()))
      print("   > Credit hours: {}".format(bestStudent.getCreditHours()))
      print("   > GPA: {:.1f}".format(bestStudent.getGPA()))


main()
