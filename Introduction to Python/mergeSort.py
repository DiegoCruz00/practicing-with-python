from random import randrange

def main():
   limit = int(input())

   exampleList = []
   for i in range(limit):
      exampleList.append(randrange(1, limit + 1))

   sortedList = sort(exampleList)

   print("[{}, ..., {}]".format(exampleList[0], exampleList[-1]))
   print("[{}, ..., {}]".format(sortedList[0], sortedList[-1]))

def sort(elementList):
   if len(elementList) < 2:
      return elementList

   elif len(elementList) == 2:
      if elementList[0] > elementList[1]:
         elementList[0], elementList[1] = elementList[1], elementList[0]

      return elementList

   else:
      n = len(elementList)
      splitLists = [elementList[:n//2], elementList[n//2:]]

      for i in range(2):
         splitLists[i] = sort(splitLists[i])

      return merge(splitLists)

def merge(lists):
   list1, list2 = lists

   mergedList = []
   while len(list1) > 0 and len(list2) > 0:
      if list1[0] < list2[0]:
         mergedList.append(list1.pop(0))
      else:
         mergedList.append(list2.pop(0))

   mergedList += list1
   mergedList += list2

   return mergedList

main()
