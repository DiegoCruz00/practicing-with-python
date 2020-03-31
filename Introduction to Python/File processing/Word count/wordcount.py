from tkinter.filedialog import askopenfilename

inputFilePath = askopenfilename()

inputFile = open(inputFilePath, "r")
print("\n Opening file at {}".format(inputFilePath))

amountOfCharacters = 0
amountOfWords = 0
amountOfLines = 0

for line in inputFile:
   amountOfCharacters += len(line)

   words = line.split()
   amountOfWords += len(words)

   amountOfLines += 1

print("\n > Characters: {}".format(amountOfCharacters))
print(" > Words: {}".format(amountOfWords))
print(" > Lines: {}\n".format(amountOfLines))
