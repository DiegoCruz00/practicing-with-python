encodedMessage = input("\nEncoded message: ")

finalMessageAsArray = []

for characterID in encodedMessage.split():
   characterIDAsInt = int(characterID)
   finalMessageAsArray.append(str(chr(characterIDAsInt)))

finalMessage = "".join(finalMessageAsArray)

print(" > The message was:\n{}".format(finalMessage))
