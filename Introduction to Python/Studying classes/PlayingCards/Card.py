class Card:
   def __init__(self, rank, suit):
      self.rank = rank
      self.suit = suit

   def getRank(self):
      return self.rank

   def getSuit(self):
      return self.suit

   def getValue(self):
      if self.rank == 1:
         return 1
      else:
         return 10

   def __str__(self):
      rankName = self._getRankName()
      suitName = self._getSuitName()

      name = rankName + " of " + suitName

      return name

   def _getRankName(self):
      if self.rank == 1:
         return "Ace"
      elif self.rank == 11:
         return "Jack"
      elif self.rank == 12:
         return "Queen"
      elif self.rank == 13:
         return "King"
      else:
         return str(self.rank)

   def _getSuitName(self):
      if self.suit == "d":
         return "Diamonds"
      elif self.suit == "c":
         return "Clubs"
      elif self.suit == "h":
         return "Hearts"
      elif self.suit == "s":
         return "Spades"
