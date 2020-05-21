import math

def main():
   try:
      a = float(input("> a: "))
      b = float(input("> b: "))
      c = float(input("> c: "))

      delta = b**2 - 4*a*c

      x1 = (-b + math.sqrt(delta)) / 2*a
      x2 = (-b - math.sqrt(delta)) / 2*a

      print("\n>>> x1 = {}\n>>> x2 = {}".format(x1, x2))

   except ValueError as exception:
      if str(exception) == "math domain error":
         print(" > No real roots")
      else:
         print(" Invalid coeficient given!")

   except:
      print(" > Sorry! Something went wrong!")


main()
