from os import system
from random import randrange
from copyToClipboard import copy

databank = {
   "Recruit": (0, 100),
   "Private": (100, 500),
   "Gefreiter": (500, 1500),
   "Corporal": (1500, 3700),
   "Master Corporal": (3700, 7100),
   "Sergeant": (7100, 12300),
   "Staff Sergeant": (12300, 20000),
   "Master Sergeant": (20000, 29000),
   "First Sergeant": (29000, 41000),
   "Sergeant-Major": (41000, 57000),
   "Warrant Officer 1": (57000, 76000),
   "Warrant Officer 2": (76000, 98000),
   "Warrant Officer 3": (98000, 125000),
   "Warrant Officer 4": (125000, 156000),
   "Warrant Officer 5": (156000, 192000),
   "Third Lieutenant": (192000, 233000),
   "Second Lieutenant": (233000, 280000),
   "First Lieutenant": (280000, 332000),
   "Captain": (332000, 390000),
   "Major": (390000, 455000),
   "Lieutenant Colonel": (455000, 527000),
   "Colonel": (527000, 606000),
   "Brigadier": (606000, 692000),
   "Major General": (692000, 787000),
   "Lieutenant General": (787000, 889000),
   "General": (889000, 1000000),
   "Marshal": (1000000, 1122000),
   "Fieldmarshal": (1122000, 1255000),
   "Commander": (1255000, 1400000),
   "Generalissimo": (1400000, 1600000),
   "Legend": (1600000, 1800000)
}

def main():
   system("cls")

   xp = getInput()

   rankName = getRank(xp)

   copy(rankName)
   print("\n" + rankName)

def getInput():
   xp = input("\n > ")

   if " " in xp:
      splitXp = xp.split()

      totalXp = 0
      for i in range(len(splitXp)):
         index = -(i + 1)
         totalXp += int(splitXp[index]) * (1000 ** i)

      return totalXp

   else:
      return int(xp)

def getRank(xp):
   if xp < databank["Legend"][0]:
      for key in databank.keys():
            low = databank[key][0]
            high = databank[key][1]

            if xp >= low and xp < high:
               return key
   else:
      legend = ((xp - databank["Legend"][0]) // 200000) + 1

      return "Legend {}".format(legend)

main()
