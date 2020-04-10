def printIntroduction():
   print("This program illustrates chaotic behaviour")

def main():
   printIntroduction()

   baseNumber1 = eval(input("Enter a number between 0 and 1: "))
   baseNumber2 = eval(input("Enter another number between 0 and 1: "))
   amountOfNumbersToPrint = int(input("How many numbers do you want to be displayed? "))

   head = "\n| index |{:^9}|{:^9}|".format(baseNumber1, baseNumber2)
   print(head)
   print("-" * (len(head) - 1))

   for printIndexLine in range(amountOfNumbersToPrint):
      baseNumber1 = 3.9 * baseNumber1 * (1 - baseNumber1)
      baseNumber2 = 3.9 * baseNumber2 * (1 - baseNumber2)

      print("|{:^7}|{:^9.5f}|{:^9.5f}|".format(printIndexLine + 1, baseNumber1, baseNumber2))

main()
