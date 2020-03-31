amountOfCents = int(input("Amount of cents: "))

print(" > {} is equal to {}.{:0>2} dollars"
      .format(amountOfCents, amountOfCents // 100, amountOfCents % 100))
