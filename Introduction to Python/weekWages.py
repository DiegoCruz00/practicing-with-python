def main():
   printIntroduction()

   while True:
      try:
         workedHours = float(input(" > Worked hours: "))
         hourlyRate = float(input(" > Hourly rate: "))

         if workedHours <= 40:
            weekWage = workedHours * hourlyRate
         else:
            weekWage = (40 * hourlyRate) + (workedHours - 40) * hourlyRate * 1.5

         print("\n  >>> Wage for the week: {:.2f}".format(weekWage))

         break

      except ValueError as exception:
         exception = str(exception)

         if exception[:34] == "could not convert string to float:":
            print("\n Oops! Invalid entry! \n\n")

      except:
         print(" Something went wrong! :(")
         break

def printIntroduction():
   print("\n  # Week Wage Calculator #  ")


main()
