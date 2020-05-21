list1 = [5, 8, 7, 1, 2, 2, 9]

def mannualSort():
   sortedList = []

   for i in range(len(list1)):
      greatestNumber = 0

      for i in range(len(list1)):
         if list1[i] > greatestNumber:
            greatestNumber = list1[i]

      sortedList.append(greatestNumber)
      list1.remove(greatestNumber)

   sortedList.reverse()

   print(sortedList)

mannualSort()
