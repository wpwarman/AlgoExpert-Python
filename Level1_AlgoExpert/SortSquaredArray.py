print("Return a Sorted, Squared Array")

def sortedSquaredArray(array):
    returnArray = []
    for x in array:
        returnArray.append(x*x)
    returnArray.sort()
    return returnArray

array = [10, 5, 15, 2, 5, 13, 22, 1]
newArray = sortedSquaredArray(array)

print("The original array:", array)
print("The sorted, squared array: ", newArray)


