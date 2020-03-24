# FORMATING INTEGERS & FLOAT NUMBERS AND STRINGS:

number = 12

# MINIMAL LENGTH:
print(f"number:10          | {number:10} |") # 10 is the minimal length of the
#                                         # space dedicated to {number:10}

# ALIGNMENTS:
print(f"number:<10         | {number:<10} |")
print(f"number:>10         | {number:>10} |")
print(f"number:^10         | {number:^10} |")

# TURN NUMBER INTO DECIMAL:
print(f"number:d           | {number:d} |")

# TURN NUMBER INTO BINARY:
print(f"number:b           | {number:b} |")

# TURN NUMBER INTO OCTAL:
print(f"number:o           | {number:o} |")

# TURN NUMBER INTO HEXADECIMAL:
print(f"number:x           | {number:x} |")

#
floatNumber = 5.7878619
print(f"floatNumber:       | {floatNumber} |")
print(f"floatNumber:f      | {floatNumber:f} |")

# LIMITING THE AMOUNT OF NUMBERS AT RIGHT OF COMMA (AUTOMATIC ROUND)
print(f"floatNumber:.2f    | {floatNumber:.2f} |")
print(f"floatNumber:.5f    | {floatNumber:.5f} |")

print(f"floatNumber:>15f   | {floatNumber:>15f} |")
print(f"floatNumber:^15f   | {floatNumber:^15f} |")

print(f"floatNumber:_<15f  | {floatNumber:_<15f} |")
print(f"floatNumber:*>15f  | {floatNumber:*>15f} |")
print(f"floatNumber:-^15f  | {floatNumber:-^15f} |")

print(f"floatNumber:0<15f  | {floatNumber:0<15f} |")
print(f"floatNumber:0>15f  | {floatNumber:0>15f} |")

#
name = "Diego"

print(f"name:10s           | {name:10s} |")

print(f"name:<10s          | {name:<10s} |")
print(f"name:>10s          | {name:>10s} |")
print(f"name:^10s          | {name:^10s} |")

print(f"name:-<10s         | {name:-<10s} |")
print(f"name:_>10s         | {name:_>10s} |")
print(f"name:m^10s         | {name:m^10s} |")

print(f"name:.4s           | {name:.4s} |")
print(f"name:.3s           | {name:.3s} |")
