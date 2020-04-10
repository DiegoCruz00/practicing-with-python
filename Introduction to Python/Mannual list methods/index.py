def index(list, searchingElement):
   for i in range(len(list)):
      if list[i] == searchingElement:
         return i

   return "Error: element not found"


def _examples():
   exampleList = [1, 2, 2, 3, 2, "a", "b", "a"]

   print(index(exampleList, "a"))
   print(index(exampleList, 4))


if __name__ == "__main__": _examples()

