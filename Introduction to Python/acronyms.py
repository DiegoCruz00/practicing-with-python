def main():
   getInputWords()
   createAcronym()
   printAcronym()

def getInputWords():
   global words
   words = input("Enter a series of words to get the acronym:\n")

def createAcronym():
   wordsAsArray = words.split()

   global acronym

   for word in wordsAsArray:
      acronym += word[0].upper()

def printAcronym():
   print(" > Acronym: {}".format(acronym))


words = ""
acronym = ""

main()
