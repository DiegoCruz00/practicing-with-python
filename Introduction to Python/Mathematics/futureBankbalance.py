print("\n\n# This program determines the value of an investment 10 years in the future.")

principal = float(input(" > Principal: "))
annualPercentageRateInDecimal = float(input(" > Annual percentage rate (in decimal): "))

print("\n Starting with {}:".format(principal))

message = ""

for year in range(10):
   principal = principal * (1 + annualPercentageRateInDecimal)
   message += "| Year {}: {:>10.3f} |\n".format(year + 1, principal)

print(message)
