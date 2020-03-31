path = "E:/Diego/ComputerScience/Programming/Training Projects/Python/Introduction to Python/File processing/"

inputFile = open(path + "names.txt", "r")
outputFile = open(path + "usernames.txt", "w")

for name in inputFile:
   if name:
      firstName, lastName = name.split()

      username = (firstName[0] + lastName[:7]).lower()

      print(username, file=outputFile)
