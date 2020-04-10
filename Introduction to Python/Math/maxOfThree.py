numbers = input().split()

maxNumber = 0

for i in range(len(numbers)):
   numbers[i] = float(numbers[i])

   if numbers[i] > maxNumber:
      maxNumber = numbers[i]

print(maxNumber)
