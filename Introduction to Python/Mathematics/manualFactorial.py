number = int(input("\nNumber: "))
factorial = 1

for i in range(number):
   factorial *= number
   number = number - 1

print(" > Factorial: {}".format(factorial))
