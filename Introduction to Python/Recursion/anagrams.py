def anagrams(string):
   string = string.upper()

   if len(string) == 0:
      return []
   elif len(string) == 1:
      return [string]

   allAnagrams = []

   for anagram in anagrams(string[1:]):
      for i in range(len(anagram) + 1):
         newAnagram = anagram[:i] + string[0] + anagram[i:]

         if newAnagram not in allAnagrams:
            allAnagrams.append(newAnagram)

   return allAnagrams


name = "Oopaa"

allAnagrams = anagrams(name)

for anagram in allAnagrams:
   print(anagram)

print("\n(showing {} anagrams)".format(len(allAnagrams)))
