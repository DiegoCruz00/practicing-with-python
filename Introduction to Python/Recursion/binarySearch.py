def search(element, elementList, startIndex=0):
   low = 0
   high = len(elementList) - 1

   if low <= high:
      middle = (high + low) // 2

      if element == elementList[middle]:
         return middle + startIndex
      elif element > elementList[middle]:
         return search(element, elementList[middle + 1:], startIndex + middle + 1)
      elif element < elementList[middle]:
         return search(element, elementList[:middle], startIndex)


print(search(4, [1, 2, 4, 8, 11, 15]))

