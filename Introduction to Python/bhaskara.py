a = float(input("> a: "))
b = float(input("> b: "))
c = float(input("> c: "))

delta = b**2 - 4*a*c

x1 = (-b + delta ** 0.5) / 2*a
x2 = (-b - delta ** 0.5) / 2*a

print("\n>>> x1 = {0}\n>>> x2 = {1}".format(x1, x2))
