def main():
   word = input()

   anagrams = getAllAnagrams(word)

   print()
   for anagram in anagrams:
      print(anagram)

   print("Showing {} anagrams...".format(len(anagrams)))

def getAllAnagrams(string):
   n = len(string)

   if n == 0:
      return []
   elif n == 1:
      return [string]
   elif n == 2:
      return [string, string[1] + string[0]]
   else:
      incompleteAnagrams = getAllAnagrams(string[1:])

      anagrams = []

      for incompleteAn in incompleteAnagrams:
         for i in range(len(incompleteAn) + 1):
            newAnagram = incompleteAn[:i] + string[0] + incompleteAn[i:]

            if newAnagram not in anagrams:
               anagrams.append(newAnagram)

      return anagrams

main()
