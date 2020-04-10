from random import randrange

def scramble(list):
   scrambledPostions = []

   for i in range(len(list)):
      while True:
         newPosition = randrange(len(list))

         if newPosition not in scrambledPostions:
            scrambledPostions.append(newPosition)
            break

   listCopy = list.copy()

   for i in range(len(scrambledPostions)):
      list.remove(listCopy[i])

      list.insert(scrambledPostions[i], listCopy[i])

   return list


def _examples():
   exampleList = [1, 2, 2, 3, 2, "a", "b", "a"]

   while True:
      newList = scramble(exampleList)

      print(newList)

      allElements = True
      for element in exampleList:
         if element not in newList:
            allElements = False

      print(allElements)

      answer = input()
      if answer.lower() == "q":
         break


if __name__ == "__main__": _examples()
