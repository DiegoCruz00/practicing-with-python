from os import system
from time import sleep

class Table:
   def __init__(self, numberOfDisks):
      self.towers = [Tower(numberOfDisks), Tower(0), Tower(0)]

   def move(self, source, destination):
      try:
         if self.validMove(source, destination):
            if self.towers[source].getAmountOfDisks() > 0:
               disk = self.towers[source].removeTopDisk()
               self.towers[destination].addDisk(disk)
         else:
            raise Exception
      except:
         return "Invalid move"

   def validMove(self, source, destination):
      sourceTopRadius = self.towers[source].getTopRadius()
      destinationTopRadius = self.towers[destination].getTopRadius()

      if destinationTopRadius > 0:
         return sourceTopRadius < destinationTopRadius
      else:
         return True

   def updateScreen(self):
      system("cls")

      for i in range(3):
         print("\n ({}) {}".format(i + 1, self.towers[i]))

   def win(self):
      return self.towers[0].getAmountOfDisks() == 0 \
         and self.towers[1].getAmountOfDisks() == 0

class Tower:
   def __init__(self, amountOfDisks):
      self.disks = []

      for radius in range(amountOfDisks, 0, -1):
         self.disks.append(Disk(radius))

   def __str__(self):
      visualTower = "|"

      for disk in self.disks:
         visualTower += " {} |".format(disk.getRadius())

      return visualTower

   def removeTopDisk(self):
      return self.disks.pop()

   def addDisk(self, disk):
      self.disks.append(disk)

   def getTopRadius(self):
      if self.getAmountOfDisks() > 0:
         return self.disks[-1].getRadius()
      else:
         return 0

   def getAmountOfDisks(self):
      return len(self.disks)

class Disk:
   def __init__(self, radius):
      self.radius = radius

   def getRadius(self):
      return self.radius

def main(mode):
   numberOfDisks = 6
   numberOfMoves = 0

   game = Table(numberOfDisks)

   if mode == "automatic":
      game.updateScreen()

      def moveTower(numberOfDisks, source, dest, temp):
         nonlocal game, numberOfMoves

         if numberOfDisks == 1:
            # input("\n/ Source: {} / Destination: {} / Temporary: {} /\n"
            #    .format(source + 1, dest + 1, temp + 1))
            game.move(source, dest)
            # game.updateScreen()

            numberOfMoves += 1
         else:
            moveTower(numberOfDisks - 1, source, temp, dest)
            moveTower(1, source, dest, temp)
            moveTower(numberOfDisks - 1, temp, dest, source)

      moveTower(numberOfDisks, 0, 2, 1)

      game.updateScreen()
      print("\n Moves: {}".format(numberOfMoves))

   elif mode == "mannual":
      while True:
         game.updateScreen()

         try:
            source, destination = int(input("\n      Source: ")), int(input(" Destination: "))
         except:
            continue

         status = game.move(source - 1, destination - 1)

         if status == "Invalid move":
            print("\n Invalid move!")
            input()
         else:
            numberOfMoves += 1

            if game.win():
               game.updateScreen()
               print("\nCongrats!")
               print("\n Moves: {}\n".format(numberOfMoves))

               break

main("automatic")
