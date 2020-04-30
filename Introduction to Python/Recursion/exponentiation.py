def expo(number, times):
   if times == 0:
      return 1
   elif times == 1:
      return number
   else:
      factor = expo(number, times // 2)

      if times % 2 == 0:
         return factor * factor
      else:
         return factor * factor * number

print(expo(2, 8))
