def main():
   print(getPrimes(1))
   print(getPrimes(3))
   print(getPrimes(10))

def getPrimes(numberOfPrimes):
   number = 1
   primesArray = []

   for i in range(numberOfPrimes):
      while True:
         number += 1
         isPrime = True

         for divisor in range(2, number):
            if isDivisible(number, divisor):
               isPrime = False
               break

         if isPrime:
            primesArray.append(number)
            break

   return primesArray

def isDivisible(_number, _divisor):
   return (_number // _divisor) == (_number / _divisor)

main()
