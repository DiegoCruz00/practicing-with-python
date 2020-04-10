def sort(list):
   sortedList = []

   for i in range(len(list)):
      lowerValue = list[0]

      for element in list:
         if element < lowerValue:
            lowerValue = element

      sortedList.append(lowerValue)
      list.remove(lowerValue)

   return sortedList


def _examples():
   exampleList = [10, 2, 4, 3, 2, -8]

   print(sort(exampleList))

if __name__ == "__main__": _examples()
