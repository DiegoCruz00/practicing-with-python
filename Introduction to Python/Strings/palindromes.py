def main():
   strings = [
      "Able was I, ere I saw Elba.",
      "Arara",
      "Arara1",
      "A man, a plan, a canal, Panama!"
   ]

   for i in range(len(strings)):
      clearString = removeInvalidCharacters(strings[i])

      print("'{}': {}".format(strings[i], isPalindrome(clearString, "loop")))

def isPalindrome(string, mode=""):
   if mode == "loop":
      string = string.lower()

      for i in range(len(string) // 2):
         if string[i] != string[-(i + 1)]:
            return False

      return True

   # Using recursion:
   else:
      n = len(string)

      if n == 0:
         return False
      elif n == 1:
         return True
      elif n == 2:
         return string[0].lower() == string[-1].lower()
      else:
         return string[0].lower() == string[-1].lower() \
            and isPalindrome(string[1:-1])


def removeInvalidCharacters(string):
   if len(string) > 0:
      invalidCharacters = """ !"#'$%&0()*+,-.\/;:<=>?@[]^-_{|}~"""

      for character in string:
         if character in invalidCharacters:
            string = string.replace(character, "")

   return string

def reverse(string):
   if len(string) < 2:
      return string
   else:
      return reverse(string[1:]) + string[0]

main()
