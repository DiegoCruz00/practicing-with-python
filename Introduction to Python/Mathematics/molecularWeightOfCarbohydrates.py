weightPerMole = {
   "H": 1.00794,
   "C": 12.0107,
   "O": 15.9994
}

print("\n\n### Molecular Weight of Carbohydrates ###\n")


numberOfHydrogenAtoms = int(input(" > H: "))
numberOfCarbonAtoms = int(input(" > C: "))
numberOfOxigenAtoms = int(input(" > O: "))

totalWeight = numberOfHydrogenAtoms * weightPerMole["H"]
totalWeight += numberOfCarbonAtoms * weightPerMole["C"]
totalWeight += numberOfOxigenAtoms * weightPerMole["O"]

print("\n >> Molecular weight: {}".format(totalWeight))
