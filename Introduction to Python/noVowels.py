sentence = input()

vowels = "aAeEiIoOuU"

finalSentence = ""

for letter in sentence:
   if letter not in vowels:
      finalSentence += letter

print(finalSentence)
