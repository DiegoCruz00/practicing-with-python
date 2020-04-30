from os import path
from tkinter.filedialog import askopenfilename

def main():
   validWords = loadValidWords()

   textFile = open(askopenfilename(), "r")

   incorrectWords = []

   for line in textFile:
      line = removeSpecialCharacters(line)
      words = line.split()

      for word in words:
         if not findWord(word.lower(), validWords):
            incorrectWords.append(word)

   for incorrectWord in incorrectWords:
      print(incorrectWord)


def loadValidWords():
   rootPath = path.dirname(path.abspath(__file__))

   wordFile = open("{}/words_alpha.txt".format(rootPath), "r")

   validWords = []
   for word in wordFile:
      validWords.append(word[:-1])

   return validWords

def removeSpecialCharacters(string):
   if len(string) > 0:
      invalidCharacters = """!"#'$%&0()*+,-.\/;:<=>?@[]^-_{|}~"""

      for character in string:
         if character in invalidCharacters:
            string = string.replace(character, "")

      return string

def findWord(word, validWords):
   low = 0
   high = len(validWords) - 1

   while low <= high:
      middle = (high + low) // 2

      if validWords[middle] == word:
         return True
      elif word > validWords[middle]:
         low = middle + 1
      elif word < validWords[middle]:
         high = middle - 1

   return False

main()
