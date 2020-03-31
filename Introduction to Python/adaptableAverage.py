def main():
   printIntroduction()

   numbers = input("\nNumbers: ").split()

   print(" > Average: {:.2f}".format(average(numbers)))

def printIntroduction():
   print("\n This algorithm calculates the average of", end="")
   print("two or more numbers separated by spaces")

def average(arrayOfNumbers):
   total = 0

   for number in arrayOfNumbers:
      total += float(number)

   average = total / len(arrayOfNumbers)

   return average


main()
