bookPrice = 24.95
discount = 0.4
shippingCost = [3, 0.75]

def getTotalWholesale(numberOfCopies):
   coverPrice = bookPrice * (1 - discount)
   saleShippingCost = shippingCost[0] + ((numberOfCopies - 1) * shippingCost[1])

   return coverPrice + saleShippingCost

priceForExampleSale = getTotalWholesale(60)

print(priceForExampleSale)
