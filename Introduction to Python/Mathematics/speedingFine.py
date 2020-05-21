def main():
   printIntroduction()
   getInputData()
   calculateStatus()
   printStatus()


def printIntroduction():
   print("\n >>> Speeding ticket fine calculator <<<")
   print("""   Policy: $50 plus $5 for each mph over the limit,
   plus a penalty of $200 for any speed over 90 mph\n""")


speedLimit, speed = 0, 0

def getInputData():
   global speedLimit, speed

   speedLimit = float(input(" > Speed limit: "))
   speed = float(input(" > Clocked speed: "))


message = ""
fine = 0

def calculateStatus():
   global message, fine

   if speed <= speedLimit:
      message = "\n  This speed was legal!"
   else:
      message = "\n  This speed was illegal!"
      fine = 50 + (speed - speedLimit) * 5

      if speed > 144:
         fine += 200

      message += "\n    > Fine: {}".format(fine)


def printStatus():
   print(message)


main()
