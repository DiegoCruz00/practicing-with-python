from tkinter.filedialog import askopenfilename

def main():
   inputFile = open(askopenfilename(), "r")

   wordCount = countAppearancesOfWords(inputFile)

   printSummary(wordCount)


def countAppearancesOfWords(file):
   wordCount = {}

   for line in file:
      line = line.split()

      for word in line:
         word = eliminateInvalidCharacters(word)

         wordCount[word] = wordCount.get(word, 0) + 1

   return wordCount


def eliminateInvalidCharacters(potentialWord):
   invalidCharacters = """!"#'$%&0()*+,-.\/;:<=>?@[]^-_{|}~"""

   cleanWord = []

   for character in potentialWord:
      if character not in invalidCharacters:
         cleanWord.append(character)

   cleanWord = "".join(cleanWord)

   return cleanWord.lower()


def printSummary(wordCountDict):
   wordCountPairs = list(wordCountDict.items())

   wordCountPairs.sort() # Sort alphabetically before frequency
   wordCountPairs.sort(key=byFrequency, reverse=True) # Sort by frequency

   for i in range(len(wordCountPairs)):
      # word, count = wordCountPairs[i]

      print(" {:>20}  {:<5}".format(*wordCountPairs[i]))


def byFrequency(pair):
   return pair[1]

main()
