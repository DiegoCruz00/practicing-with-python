from math import radians, cos, sin

def main():
   angle, velocity, height, time = getInputs()

   cannonball = Projectile(angle, velocity, height)
   cannonball.updatePositions(time)

   printSummary(time, cannonball)


class Projectile:
   def __init__(self, angle, velocity, height):
      self.xPosition = 0
      self.initialHeight = height
      self.yPosition = height

      self.xVelocity, self.yVelocity = self._getComponents(angle, velocity)

   def _getComponents(self, angle, velocity):
      theta = radians(angle)
      xVelocity = velocity * cos(theta)
      yVelocity = velocity * sin(theta)

      return xVelocity, yVelocity

   def _getTimeToMaxHeight(self):
      return self.yVelocity / 9.8

   def getX(self):
      return self.xPosition

   def getY(self):
      return self.yPosition

   def updatePositions(self, timeInterval):
      self.xPosition = self.xVelocity * timeInterval
      self.yPosition += self.yVelocity * timeInterval - (9.8 * timeInterval ** 2) / 2

   def getMaxHeight(self):
      t = self._getTimeToMaxHeight()

      maxHeight = self.initialHeight + self.yVelocity * t - ((9.8 * t ** 2) / 2)
      return maxHeight

   def getMaxHorizontalDistance(self):
      t = 2 * self._getTimeToMaxHeight()

      maxHorizontalDistance = self.xVelocity * t
      return maxHorizontalDistance


def getInputs():
   angle = float(input("Launch angle (in degrees): "))
   velocity = float(input("Initial velocity (in m/s): "))
   height = float(input("Initial height (in meters): "))
   time = float(input("Time interval (in seconds): "))

   return angle, velocity, height, time


def printSummary(time, projectile):
   print("\n > At {} seconds, the cannonball was at: ".format(time))
   print("    Height: {:.2f} m".format(projectile.getY()))
   print("    Horizontal distance: {:.2f} m".format(projectile.getX()))

   print("\n > The maximum height for this cannonball is: ", end="")
   print("{:.2f} m".format(projectile.getMaxHeight()))

   print(" > The maximum horizontal distance for this cannonball is: ", end="")
   print("{:.2f} m".format(projectile.getMaxHorizontalDistance()))


main()
