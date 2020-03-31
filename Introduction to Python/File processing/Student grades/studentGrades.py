from tkinter.filedialog import askopenfilename

inputFilePath = askopenfilename()

inputFile = open(inputFilePath, "r")
print("\n Opening file at {}".format(inputFilePath))

message = "\n"

for line in inputFile:
   student, grade = line.split()
   message += " > {:>10}: {} ({})\n".format(student[:10], int(grade) * ":", grade)

print(message)
