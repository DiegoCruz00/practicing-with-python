def removeDuplicates(currentList):
   copyCurrentList = currentList.copy()

   for element in copyCurrentList:
      appearances = currentList.count(element)

      if appearances > 1:
         firstIndex = currentList.index(element)

         for i in range(appearances):
            currentList.remove(element)

         currentList.insert(firstIndex, element)

   return currentList


def _examples():
   exampleList = [1, 2, 1, 1, 5, 4, 5]

   exampleList = removeDuplicates(exampleList)
   print(exampleList)

if __name__ == "__main__": _examples()
