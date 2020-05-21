def main():
   printIntroduction()
   getInputData()
   calculateBMI()
   printHealthyStatus()

def printIntroduction():
   print("\n >>> BMI (Body Mass Index) Calculator <<<")

weight, height = 0, 0

def getInputData():
   global weight, height
   weight = float(input(" > Weight (in kg): "))
   height = float(input(" > Height (in meters): "))

bmi = 0

def calculateBMI():
   global bmi

   bmi = weight / (height ** 2)

def printHealthyStatus():
   if bmi > 25:
      message = "\n   You are overweight!"
   elif bmi < 19:
      message = "\n   You are underweight!"
   else:
      message = "\n   Congratualtions! You are healthy!"

   message += "\n    > BMI: {:.2f}".format(bmi)

   print(message)

main()
