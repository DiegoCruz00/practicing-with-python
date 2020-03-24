def getAverage(arrayOfNumbers):
   arrayOfNumbers = arrayOfNumbers.split(" ")
   total = 0

   for i in range(len(arrayOfNumbers)):
      total += float(arrayOfNumbers[i])

   average = total / len(arrayOfNumbers)

   return average


numbers = input()

print(getAverage(numbers))
