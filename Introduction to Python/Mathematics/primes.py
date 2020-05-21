def findAllPrimesUpTo(n):
   allNumbers = list(range(2, n + 1))
   primes = []

   while len(allNumbers) > 0:
      primes.append(allNumbers[0])
      allNumbers.pop(0)

      for number in allNumbers.copy():
         if number % primes[-1] == 0:
            allNumbers.remove(number)

   return primes


n = int(input())

print(findAllPrimesUpTo(n))
