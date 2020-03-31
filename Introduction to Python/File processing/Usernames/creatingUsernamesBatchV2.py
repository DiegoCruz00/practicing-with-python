from tkinter.filedialog import askopenfilename, asksaveasfilename

inputPath = askopenfilename()
outputPath = asksaveasfilename()

inputFile = open(inputPath, "r")
outputFile = open(outputPath, "w")

print("\nOpening file at {}".format(inputPath))

for name in inputFile:
   if name:
      firstName, lastName = name.split()

      username = (firstName[0] + lastName[:7]).lower()

      print(username, file=outputFile)

print("\nSaving file at {}".format(outputFile.name))
print("\nFile saved!")

inputFile.close()
outputFile.close()
