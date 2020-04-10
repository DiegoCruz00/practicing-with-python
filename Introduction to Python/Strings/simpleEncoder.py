rawMessage = input("\nType the message to encode: ")

encodedMessageAsArray = []

for letter in rawMessage:
   encodedMessageAsArray.append(str(ord(letter)))

finalEncodedMessage = " ".join(encodedMessageAsArray)

print(" > Encoded message:\n{}".format(finalEncodedMessage))
