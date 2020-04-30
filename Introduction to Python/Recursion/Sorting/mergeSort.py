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
   if len(elementList) == 1:
      return elementList

   elif len(elementList) == 2:
      if elementList[0] > elementList[1]:
         elementList[0], elementList[1] = elementList[1], elementList[0]

      return elementList

   else:
      n = len(elementList)
      splitedLists = [elementList[:n//2], elementList[n//2:]]

      for i in range(2):
         splitedLists[i] = sort(splitedLists[i])

      sortedList = mergeLists(splitedLists[0], splitedLists[1])

      return sortedList

def mergeLists(list1, list2):
   mergedList = []

   while len(list1) > 0 and len(list2) > 0:
      if list1[0] < list2[0]:
         mergedList.append(list1[0])
         list1.pop(0)
      else:
         mergedList.append(list2[0])
         list2.pop(0)

   mergedList += list1
   mergedList += list2

   return mergedList

main()
