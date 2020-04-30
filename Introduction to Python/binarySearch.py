def search(element, listOfElements):
   low = 0
   high = len(listOfElements) - 1

   while low <= high:
      middle = (high + low) // 2

      if element == listOfElements[middle]:
         return middle
      elif element > listOfElements[middle]:
         low = middle + 1
      elif element < listOfElements[middle]:
         high = middle - 1

exampleList = range(10)

print(search(1, exampleList))
