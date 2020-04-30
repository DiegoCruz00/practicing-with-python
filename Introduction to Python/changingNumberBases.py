def main():
   number, sourceBase, targetBase = getInputs()

   result = changeBase(number, sourceBase, targetBase)

   if result:
      print("\n Result: {}".format(result))
   else:
      print("\n Invalid entry! {} is not a base {} number!".format(number, sourceBase))

def getInputs():
   number = str(input("\n> Number: "))
   sourceBase = int(input("> From base: "))
   targetBase = int(input("> To base: "))

   return number, sourceBase, targetBase

def changeBase(number, sourceBase, targetBase):
   if validNumber(number, sourceBase):
      if targetBase == 10:
         numberAsString = str(number)

         possibleCharacters = createAllValidAlgs(sourceBase)

         total = 0
         for i in range(len(numberAsString)):
            prospeciveAlg = numberAsString[-(i + 1)]

            try:
               alg = int(prospeciveAlg)
            except:
               alg = possibleCharacters.index(prospeciveAlg)

            total += alg * (sourceBase ** i)

         return total

      elif sourceBase == 10:
         number = int(number)

         possibleCharacters = createAllValidAlgs(targetBase)

         algs = []
         while number > 0:
            remainder = number % targetBase

            if remainder > 9:
               algs.append(str(possibleCharacters[remainder]))
            else:
               algs.append(str(remainder))

            number = number // targetBase

         algs.reverse()

         return "".join(algs)

      else:
         numberInBase10 = changeBase(number, sourceBase, 10)
         result = changeBase(numberInBase10, 10, targetBase)

         return result

def validNumber(number, base):
   possibleCharacters = createAllValidAlgs(base)

   for i in range(len(possibleCharacters)):
      possibleCharacters[i] = str(possibleCharacters[i])

   for alg in str(number):
      if alg not in possibleCharacters:
         return False

   return True

def createAllValidAlgs(base):
   if base > 10:
      possibleCharacters = list(range(10))

      for i in range(base - 10):
         possibleCharacters.append(chr(97 + i))
   else:
      possibleCharacters = list(range(base))

   return possibleCharacters

main()
