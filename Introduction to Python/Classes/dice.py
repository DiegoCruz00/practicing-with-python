from random import randrange

class Die:
   def __init__(self, sides):
      self.sides = sides
      self.value = 1

   def roll(self):
      self.value = randrange(1, self.sides + 1)

   def setValue(self, value):
      if value <= self.sides:
         self.value = value

die1 = Die(6)
die2 = Die(10)

print(die1.sides)
print(die1.value)
die1.roll()
print(die1.sides)
print(die1.value)

print()

print(die2.sides)
print(die2.value)
die2.roll()
print(die2.sides)
print(die2.value)
