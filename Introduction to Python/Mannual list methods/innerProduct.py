def innerProduct(list1, list2):
   if len(list1) == len(list2):
      total = 0

      for i in range(len(list1)):
         total += list1[i] * list2[i]

      return total

def _examples():
   list1 = [1, 2, 3, 4]
   list2 = [2, 1, 3, 2]

   print(innerProduct(list1, list2))

if __name__ == "__main__": _examples()
