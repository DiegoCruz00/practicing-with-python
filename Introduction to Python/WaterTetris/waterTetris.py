import os

class EnergyCalculator:
   def __init__(self, blockArena):
      self.arena = blockArena

   def getEnergyLeft(self):
      lowestTower, highestTower = self.getExtremes()

      highestEnergyLevel = len(lowestTower)

      levelBoundaryIndexes = [0, 0]
      for i in range(1, len(highestTower)): # For every height
         nextLevelAllowed = [False, False]

         for j in range(len(self.arena)): # For every block at current height
            if not nextLevelAllowed[0] and j < self.arena.index(lowestTower) and len(self.arena[j]) > highestEnergyLevel:
               nextLevelAllowed[0] = True
               levelBoundaryIndexes[0] = j
               continue

            if not nextLevelAllowed[1] and j > self.arena.index(lowestTower) and len(self.arena[j]) > highestEnergyLevel:
               nextLevelAllowed[1] = True
               levelBoundaryIndexes[1] = j
               break

         if nextLevelAllowed[0] and nextLevelAllowed[1]:
            highestEnergyLevel += 1
         else:
            break

      totalEnergyLeft = 0

      for i in range(len(self.arena)):
         if i > levelBoundaryIndexes[0] and i < levelBoundaryIndexes[1]:
            totalEnergyLeft += highestEnergyLevel - len(self.arena[i])

      return totalEnergyLeft

   def getExtremes(self):
      lowestTower, highestTower = self.arena[0], self.arena[0]

      for i in range(1, len(self.arena)):
         if self.arena[i] < lowestTower:
            lowestTower = self.arena[i]
         if self.arena[i] > highestTower:
            highestTower = self.arena[i]

      return lowestTower, highestTower

def main():
   currentFolderPath = os.path.dirname(os.path.abspath(__file__))
   arenaFile = open("{}/arena.txt".format(currentFolderPath), "r")

   arena = []
   for block in arenaFile:
      arena.append(block)

   app = EnergyCalculator(arena)
   print(app.getEnergyLeft())


if __name__ == "__main__":
   main()
