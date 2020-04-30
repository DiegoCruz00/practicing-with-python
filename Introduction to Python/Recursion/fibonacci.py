from time import time

def fibonacci(n):
   currentNumber = 1
   nextNumber = 1

   for i in range(n - 1):
      currentNumber, nextNumber = nextNumber, nextNumber + currentNumber

   return currentNumber

def fib(n):
   if n < 3:
      return 1
   else:
      return fib(n - 1) + fib(n - 2)

# Efficient version
currentTime = time()
print(fibonacci(30))
print(time() - currentTime)

# Very inneficient version
currentTime = time()
print(fib(30))
print(time() - currentTime)
