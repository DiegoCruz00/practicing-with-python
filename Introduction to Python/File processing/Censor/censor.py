from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
   textFile, wordsToCensorFile, outputFile = getInputs()

   wordsToCensor = []

   for word in wordsToCensorFile:
      wordsToCensor.append(word[:-1])

   for line in textFile:
      for censorWord in wordsToCensor:
         line = line.replace(censorWord.lower(), "*" * len(censorWord))
         line = line.replace(censorWord.title(), "*" * len(censorWord))
         line = line.replace(censorWord.upper(), "*" * len(censorWord))

      print(line, file=outputFile, end="")

def getInputs():
   textFile = open(askopenfilename(), "r")
   wordsToCensorFile = open(askopenfilename(), "r")
   outputFile = open(asksaveasfilename(), "w")

   return textFile, wordsToCensorFile, outputFile

main()
