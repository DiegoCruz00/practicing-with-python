import os

currentFolderPath = os.path.dirname(os.path.abspath(__file__))
#                              ^               ^
#                              ^       Get the path of the current file
#                 Get the folder in which this file is located

print(currentFolderPath)
