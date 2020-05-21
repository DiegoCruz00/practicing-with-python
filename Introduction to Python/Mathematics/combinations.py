def main():
   print("\nThis program computes combinations:")
   n, p = getInputs()
   combinations = int(fact(n) / (fact(p) * fact(n - p)))
   printResult(combinations)

def getInputs():
   n = int(input(" > n: "))
   p = int(input(" > p: "))

   return n, p

def fact(number):
   total = 1
   for i in range(2, number + 1):
      total *= i

   return total

def printResult(combinations):
   print("\n Possible combinations: {}".format(combinations))


main()
