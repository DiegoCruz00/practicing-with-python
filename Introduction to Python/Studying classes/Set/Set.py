class Set:
   def __init__(self, elements):
      self.elements = elements

   def addElement(self, element):
      self.elements.append(element)

   def deleteElement(self, element):
      self.elements.remove(element)

   def member(self, element):
      return self.elements.count(element) > 0

   def intersection(self, givenSet):
      listIntersection = []

      for element in self.elements:
         if element in givenSet.elements:
            listIntersection.append(element)

      return Set(listIntersection)

   def union(self, givenSet):
      return Set(self.elements + givenSet.elements)

   def subtract(self, givenSet):
      subtractedList = []

      for element in self.elements:
         if element not in givenSet.elements:
            subtractedList.append(element)

      return Set(subtractedList)

   def __str__(self):
      return str(self.elements)


set1 = Set([1, 2, 3])
set2 = Set([3, 4])

set3 = set1.union(set2)

print(set3)
