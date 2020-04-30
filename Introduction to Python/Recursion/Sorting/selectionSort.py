from random import randrange
from time import time

def main():
   # exampleList = []
   # for i in range(10):
   #    exampleList.append(randrange(1, 101))

   exampleList = [79, 92, 57, 83, 13, 72, 11, 19, 19, 68]

   currentTime = time()

   print(exampleList)
   exampleList = sort(exampleList)
   print(exampleList)

   print("{:.30f}".format(time() - currentTime))


def sort(elementList):
   sortedList = []

   for i in range(len(elementList)):
      lowest = findLowest(elementList)

      sortedList.append(lowest)
      elementList.remove(lowest)

   return sortedList

def findLowest(elementList):
   lowest = elementList[0]

   for i in range(1, len(elementList)):
      if elementList[i] < lowest:
         lowest = elementList[i]

   return lowest

main()
