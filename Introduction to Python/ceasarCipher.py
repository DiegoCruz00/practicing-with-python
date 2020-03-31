def encode():
   messageToCipher = input(""" > Message to encode using Caesar cipher
      (use only letters - no special characters):\n""")
   key = int(input(" > Key to cipher: "))

   encodedMessage = ""

   for letter in messageToCipher:
      if letter == " ":
         encodedMessage += " "
      else:
         encodedLetterID = ord(letter) + key

         if letter == letter.upper():
            while encodedLetterID > 90:
               encodedLetterID -= 26
         else:
            while encodedLetterID > 122:
               encodedLetterID -= 26

         encodedMessage += chr(encodedLetterID)

   print("\nThe ciphered message is:\n{}".format(encodedMessage))

def decode():
   messageToDecode = input(""" > Message to encode using Caesar cipher
      (use only letters - no special characters):\n""")
   key = int(input(" > Key to decode: "))

   decodedMessage = ""

   for letter in messageToDecode:
      if letter == " ":
         decodedMessage += " "
      else:
         decodedLetterID = ord(letter) - key

         if letter == letter.upper():
            while decodedLetterID < 65:
               decodedLetterID += 26
         else:
            while decodedLetterID < 97:
               decodedLetterID += 26

         decodedMessage += chr(decodedLetterID)

   print("\nThe message was:\n{}".format(decodedMessage))


answer = input("""\n > Do you want to encode or decode a Caesar-ciphered message?
   ( e to encode | d to decode): """)

if answer.lower() == "e":
   encode()
elif answer.lower() == "d":
   decode()
