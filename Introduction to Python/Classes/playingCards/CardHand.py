from Card import Card

class CardHand:
   def __init__(self, listOfCards):
      self.cards = listOfCards.copy()

   def sort(self):
      self.cards.sort(key=Card.getRank)
      self.cards.sort(key=Card.getSuit)

   def getCategory(self):
      if self._isRoyalFlush():
         return "Royal Flush"
      if self._isStraightFlush():
         return "Straight Flush"
      if self._cardsOfTheSameSuit():
         return "Flush"
      if self._ranksInARow():
         return "Straight"
      if self._isFourOfAKind():
         return "Four of a Kind"
      if self._isFullHouse():
         return "Full House"
      if self._isThreeOfAKind():
         return "Three of a Kind"
      if self._isTwoPairs():
         return "Two Pairs"
      if self._isPair():
         return "Pair"

      return str(self._highestRank()) + " High"


   def _isRoyalFlush(self):
      royalFlush = self._cardsOfTheSameSuit()

      for rank in ["1", "10", "11", "12", "13"]:
         royalFlush = royalFlush and self._countCard(rank) == 1

      return royalFlush

   def _isStraightFlush(self):
      return self._cardsOfTheSameSuit() and self._ranksInARow()

   def _isFourOfAKind(self):
      verifyingRank = str(self.cards[0].getRank())

      if self._countCard(verifyingRank) == 4:
         return True
      else:
         verifyingRank = str(self.cards[1].getRank())

         if self._countCard(verifyingRank) == 4:
            return True
         else:
            return False

   def _isFullHouse(self):
      allRanks = []

      for card in self.cards:
         if card.getRank() not in allRanks:
            allRanks.append(card.getRank())

      if len(allRanks) == 2:
         countRanks = [0, 0]

         for i in range(2):
            for card in self.cards:
               if card.getRank() == allRanks[i]:
                  countRanks[i] += 1

         if 3 in countRanks and 2 in countRanks:
            return True

   def _isThreeOfAKind(self):
      ranks = self._getUniqueRanks()

      for rank in ranks:
         if self._countCard(str(rank)) == 3:
            return True

      return False

   def _isTwoPairs(self):
      ranks = self._getUniqueRanks()

      if len(ranks) == 3:
         cardGroups = [0, 0, 0]

         for i in range(3):
            for card in self.cards:
               if card.getRank() == ranks[i]:
                  cardGroups[i] += 1

         if cardGroups.count(2) == 2 and cardGroups.count(1) == 1:
            return True

   def _isPair(self):
      ranks = self._getUniqueRanks()

      cardGroups = []

      for rank in ranks:
         cardGroups.append(self._countCard(str(rank)))

      return cardGroups.count(2) == 1


   def _highestRank(self):
      ranks = self._getUniqueRanks()
      ranks.sort()

      return ranks[-1]

   def _cardsOfTheSameSuit(self):
      oneSuit = True
      suit = self.cards[0].getSuit()

      for i in range(1, len(self.cards)):
         if suit != self.cards[i].getSuit():
            oneSuit = False
            break

      return oneSuit

   def _countCard(self, card):
      count = 0

      if card.isnumeric():
         for currentCard in self.cards:
            if currentCard.getRank() == int(card):
               count += 1

      elif card.count(" ") == 2:
         for currentCard in self.cards:
            if currentCard == card:
               count += 1
      else:
         for currentCard in self.cards:
            if currentCard.getSuit() == card:
               count += 1

      return count

   def _ranksInARow(self):
      ranks = []

      for card in self.cards:
         ranks.append(card.getRank())

      ranks.sort()

      return ranks == list(range(ranks[0], ranks[0] + 5))

   def _getUniqueRanks(self):
      ranks = []

      for card in self.cards:
         if card.getRank() not in ranks:
            ranks.append(card.getRank())

      return ranks
