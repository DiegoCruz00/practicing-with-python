stopPosition = int(input())

sequence = [1, 1]

for i in range(stopPosition - 1):
   nextNumber = sequence[0] + sequence[1]

   sequence[0] = sequence[1]
   sequence[1] = nextNumber

print(sequence[0])
