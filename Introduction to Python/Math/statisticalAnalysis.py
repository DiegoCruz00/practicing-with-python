def main():
   _printIntro()

   numbers = _getNumbers()

   mean = getMean(numbers)
   median = getMedian(numbers)
   standardDeviation = getStandardDeviation(numbers)

   print("   Mean: {:.2f}".format(mean))
   print("   Median: {:.2f}".format(median))
   print("   Standard Deviation: {:.2f}".format(standardDeviation))


def _printIntro():
   print("\nEnter a series of numbers to see their statistical analysis:")
   print("      (Enter a blank line to end input)")


def _getNumbers():
   numbers = []

   while True:
      inputLine = input(" > ")

      if inputLine:
         numbers.append(float(inputLine))
      else:
         break

   return numbers


def getMean(listOfNumbers):
   total = 0

   for number in listOfNumbers:
      total += number

   return total / len(listOfNumbers)


def getMedian(listOfNumbers):
   listOfNumbers.sort()

   size = len(listOfNumbers)
   index = size // 2

   if size % 2 == 0:
      return (listOfNumbers[index] + listOfNumbers[index - 1]) / 2
   else:
      return listOfNumbers[size // 2]


def getStandardDeviation(listOfNumbers):
   mean = getMean(listOfNumbers)

   deviation = 0

   for number in listOfNumbers:
      currentDeviation = (mean - number) ** 2
      deviation += currentDeviation

   variance = deviation / len(listOfNumbers)

   standardDeviation = (variance) ** 0.5

   return standardDeviation


if __name__ == "__main__": main()
