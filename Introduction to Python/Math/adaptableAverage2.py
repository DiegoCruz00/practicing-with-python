numbers = []
average = 0

def main():
   printIntroduction()
   getInputNumbers()
   calculareAverage()
   printAverage()

def printIntroduction():
   print("\n This program calculares the average of numbers")
   print("  (Enter a number per line and type -1 to get the average)\n")

def getInputNumbers():
   global numbers

   while True:
      inputNumber = float(input())

      if inputNumber == - 1.0:
         break
      else:
         numbers.append(inputNumber)

def calculareAverage():
   global average
   total = 0

   for number in numbers:
      total += number

   average = total / len(numbers)

def printAverage():
   print(" > Average: {:.2f}".format(average))


main()
