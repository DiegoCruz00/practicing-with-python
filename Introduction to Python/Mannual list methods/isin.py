def isIn(list, searchingElement):
   for element in list:
      if element == searchingElement:
         return True

   return False


def _examples():
   exampleList = [1, 2, 2, 3, 2, "a", "b", "a"]

   print(isIn(exampleList, "b"))
   print(isIn(exampleList, 4))


if __name__ == "__main__": _examples()
