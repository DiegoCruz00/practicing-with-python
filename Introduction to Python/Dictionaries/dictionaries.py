from tkinter.filedialog import askopenfilename

inputFile = open(askopenfilename(), "r")

userData = {}

for line in inputFile:
   user, password = line.split(", ")

   userData[user] = password[:-1]

print(userData)
