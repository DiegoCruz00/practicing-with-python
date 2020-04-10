def isATriangle():
   return shortestSide + middleSide > longestSide

longestSide, middleSide, shortestSide = 0, 0, 0

print("\n This algorithm calculares the area of a triangle given the length of its sides!\n")

while True:
   triangleSides = input(" > Sides of the triangle (separated by spaces): ").split()

   for i in range(3):
      triangleSides[i] = float(triangleSides[i])

   longestSide = max(triangleSides)
   triangleSides.remove(longestSide)

   shortestSide = min(triangleSides)
   triangleSides.remove(shortestSide)

   middleSide = triangleSides[0]

   if isATriangle(): break
   else:
      print("\n This is not a triangle! Try again!\n\n")

a, b, c = longestSide, middleSide, shortestSide

p = (a + b + c) / 2

area = (p * (p - a) * (p - b) * (p - c))**0.5

print("   >> Area: {:.2f}".format(area))
