def amountOfRectangles(xLength, yLength):

   def rectangleInsideArea(length, height):
      return (length <= xLength - 1) \
         and (height <= yLength - 1)

   total = 0

   for comparingXSize in range(1, xLength):
      for comparingYSize in range(1, yLength):
         for x in range(xLength - 1):
            for y in range(yLength - 1):
               if rectangleInsideArea(x + comparingXSize, y + comparingYSize):
                  total += 1
               else: break

   return total

def test():
   testCases = [
      [(0, 0), 0],
      [(2, 3), 3],
      [(3, 4), 18],
      [(5, 3), 30],
      [(3, 5), 30],
      [(4, 4), 36],
      [(12, 28), 24948],
   ]

   for test in testCases:
      result = amountOfRectangles(*test[0])

      print("({}, {}) -> {} ({})".format(*test[0], result, result == test[1]))

test()
