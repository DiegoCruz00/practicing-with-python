from tkinter.filedialog import askopenfilename, asksaveasfilename
from Card import Card
from CardHand import CardHand

def main():
   inputFile, outputFile = getInputFiles()

   listOfCards = getCardsFrom(inputFile)

   cardHand = CardHand(listOfCards)
   cardHand.sort()

   category = cardHand.getCategory()

   for card in cardHand.cards:
      print(card, file=outputFile)

   print("\n" + category, file=outputFile)


def getInputFiles():
   inputFile = open(askopenfilename(), "r")
   outputFile = open(asksaveasfilename(), "w")

   return inputFile, outputFile


def getCardsFrom(file):
   cards = []

   for line in file:
      rank, suit = line.split()
      cards.append(Card(int(rank), suit))

   return cards


main()
