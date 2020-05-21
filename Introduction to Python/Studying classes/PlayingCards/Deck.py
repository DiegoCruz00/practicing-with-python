from random import randrange
from Card import Card

class Deck:
   def __init__(self):
      self.cards = self._createAllCards()

   def _createAllCards(self):
      cards = []

      for suit in ["d", "s", "h", "c"]:
         for rank in range(1, 14):
            cards.append(Card(rank, suit))

      return cards

   def shuffle(self):
      newPositions = []
      cardsListCopy = self.cards.copy()
      size = len(self.cards)

      for i in range(size):
         while True:
            position = randrange(size)

            if position not in newPositions:
               newPositions.append(position)
               break

      for i in range(size):
         self.cards.remove(cardsListCopy[i])
         self.cards.insert(newPositions[i], cardsListCopy[i])

   def dealCard(self):
      if self.cardsLeft() > 0:
         return self.cards.pop(0)

   def cardsLeft(self):
      return len(self.cards)

   def test(self):
      print("OK")

def _examples():
   deck1 = Deck()
   deck1.shuffle()

   deals = int(input("> Number of deals: "))

   summary = "\n"

   for i in range(deals):
      card = deck1.dealCard()

      if card:
         summary += str(card) + "\n"

   summary += "\n{} cards left".format(deck1.cardsLeft())

   print(summary)

_examples()
