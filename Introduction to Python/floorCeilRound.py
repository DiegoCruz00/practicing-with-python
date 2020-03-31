testNumber = 541.1897987

print("Number: {}\n".format(testNumber))

import math

print("Floor: {}".format(math.floor(testNumber))) # Arredonda para baixo
print("Ceil: {}".format(math.ceil(testNumber))) # Arredonda para cima
print("Round: {}".format(round(testNumber))) # Arredonda para o mais próximo
print("Round: {}".format(round(testNumber, 2))) # Arredonda para o mais próximo
#                                                com duas casas decimais
print("Round: {}".format(round(testNumber, -1))) # Arredonda também uma
print("Round: {}".format(round(testNumber, -2))) # quantidade de números antes
#                                                  da vírgula
