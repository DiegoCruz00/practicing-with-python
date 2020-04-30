from time import time
from random import randrange

def main():
   limit = 1000
   elapsedLinearTime, elapsedBinaryTime, elapsedRecursiveTime = 0, 0, 0

   exampleList = list(range(limit))

   for i in range(1000):
      searchingNumber = randrange(limit)

      print("Searching for {}:".format(searchingNumber))

      startingTime = time()
      linearSearch(searchingNumber, exampleList)
      elapsedLinearTime += time() - startingTime

      startingTime = time()
      binarySearch(searchingNumber, exampleList)
      elapsedBinaryTime += time() - startingTime

      startingTime = time()
      recursiveBinarySearch(searchingNumber, exampleList)
      elapsedRecursiveTime += time() - startingTime

   print("\n  Linear time: {:.15f} s".format(elapsedLinearTime))
   print("  Binary time: {:.15f} s".format(elapsedBinaryTime))
   print("  Recursive time: {:.15f} s".format(elapsedRecursiveTime))


def linearSearch(element, listOfElements):
   for i in range(len(listOfElements)):
      if listOfElements[i] == element:
         return i

def binarySearch(element, listOfElements):
   low = 0
   high = len(listOfElements) - 1

   while low <= high:
      middleIndex = (high + low) // 2

      if listOfElements[middleIndex] == element:
         return middleIndex
      elif listOfElements[middleIndex] > element:
         high = middleIndex - 1
      elif listOfElements[middleIndex] < element:
         low = middleIndex + 1

def recursiveBinarySearch(element, elementList, startIndex=0):
   low = 0
   high = len(elementList) - 1

   if low <= high:
      middle = (high + low) // 2

      if element == elementList[middle]:
         return middle + startIndex
      elif element > elementList[middle]:
         return recursiveBinarySearch(element, elementList[middle + 1:], startIndex + middle + 1)
      elif element < elementList[middle]:
         return recursiveBinarySearch(element, elementList[:middle], startIndex)

main()
