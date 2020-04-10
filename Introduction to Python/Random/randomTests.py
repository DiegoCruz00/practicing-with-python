from random import random, randrange, choice, uniform

print(randrange(1, 11))
print(random() - 0.5)
print(uniform(-10, 10))

print(randrange(1, 7))       # These two lines get
print(choice(range(1, 7)))   # have the same meaning

dice1 = randrange(1, 7)
dice2 = randrange(1, 7)
print(dice1 + dice2)
