def findAllIndexes(currentList, searchingValue):
    """ Return a list with all indexes of a searching value in a given list

        This example

            list1 = [1, 2, 3, 2]
            indexesOf2 = findAllIndexes(list1, 2)
            print(indexesOf2)

        will print [1, 3]."""

    indexes = []

    for index in range(len(currentList)):
        if currentList[index] == searchingValue:
            indexes.append(index)

    return indexes

