def reverse(list):
   reversedList = []

   for i in range(len(list) - 1, -1, -1):
      reversedList.append(list[i])

   return reversedList


def _examples():
   exampleList = [1, 2, 2, 3, 2, "a", "b", "a"]

   print(reverse(exampleList))

if __name__ == "__main__": _examples()
