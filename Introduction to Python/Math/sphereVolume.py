import math

def getSphereVolume(radius):
   return (4 / 3) * math.pi * (radius ** 3)

sphereVolume = getSphereVolume(float(input("> Sphere radius: ")))

print(">>> %.3f" % (sphereVolume))
