def count(list, elementToBeCounted):
   count = 0

   for element in list:
      if element == elementToBeCounted:
         count += 1

   return count


def _examples():
   exampleList = [1, 2, 2, 3, 2, "a", "b", "a"]

   print(count(exampleList, "a"))
   print(count(exampleList, 0))


if __name__ == "__main__": _examples()
