from random import randrange

class Dice:
   def __init__(self):
      self.dice = [0] * 5
      self.rollAll()

   def roll(self, indexList):
      for index in indexList:
         self.dice[index] = randrange(1, 7)

   def rollAll(self):
      self.roll(range(5))

   def getValues(self):
      return self.dice.copy()

   def getPayoff(self):
      if self._isFiveOfAKind():
         return ("Five of a Kind", 30)
      if self._isStraight():
         return ("Straight", 20)
      if self._isFourOfAKind():
         return ("Four of a Kind", 15)
      if self._isFullHouse():
         return ("Full House", 12)
      if self._isThreeOfAKind():
         return ("Three of a Kind", 8)
      if self._isTwoPairs():
         return ("Two Pairs", 5)

      return ("Garbage", 0)


   def _isFiveOfAKind(self):
      kind = self.dice[0]

      return self.dice.count(kind) == 5

   def _isStraight(self):
      diceGroup = self.dice.copy()
      diceGroup.sort()

      return diceGroup == list(range(diceGroup[0], diceGroup[0] + 5))

   def _isFourOfAKind(self):
      for die in self.dice:
         if self.dice.count(die) == 4:
            return True

   def _isFullHouse(self):
      groups = []

      for die in self.dice:
         if self.dice.count(die) == 2 and 2 not in groups:
            groups.append(2)
         elif self.dice.count(die) == 3 and 3 not in groups:
            groups.append(3)

      return 2 in groups and 3 in groups

   def _isThreeOfAKind(self):
      for die in self.dice:
         if self.dice.count(die) == 3:
            return True

   def _isTwoPairs(self):
      pairKinds = []

      for die in self.dice:
         if self.dice.count(die) == 2 and die not in pairKinds:
            pairKinds.append(die)

      return len(pairKinds) == 2
