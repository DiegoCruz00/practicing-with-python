from random import choice

def main():
   length = int(input())

   currentPosition = 0
   stepsByPosition = [0] * length

   sidewalk = getSidewalkList(length)
   centerIndex = sidewalk.index(0)

   stepsByPosition[centerIndex] = 1

   while True:
      move = choice([-1, 1])

      currentPosition += move

      if currentPosition not in sidewalk:
         break

      currentIndex = sidewalk.index(currentPosition)
      stepsByPosition[currentIndex] += 1

   printSummary(stepsByPosition, centerIndex)


def getSidewalkList(length):
   if length % 2 == 0:
      start = int(- (length / 2))
      end = int(length / 2)

      return list(range(start, end))

   else:
      start = int(- (length - 1) / 2)
      end = int(((length - 1) / 2) + 1)

      return list(range(start, end))


def printSummary(stepsByPosition, centerIndex):
   print("\nTotal steps: {}".format(sum(stepsByPosition)))

   visualSidewalk = "\n|"

   for i in range(len(stepsByPosition)):
      if i == centerIndex:
         visualSidewalk += " ({}) |".format(stepsByPosition[i])
      else:
         visualSidewalk += " {} |".format(stepsByPosition[i])

   print(visualSidewalk)


main()
