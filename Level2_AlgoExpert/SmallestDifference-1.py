print("Smallest Difference")

def smallestDifference(arrayOne, arrayTwo):
    #array1.sort(reverse=True)
    #array2.sort(reverse=True)
    #smallestDelta = array1[0] + array2[0] + 1
    smallestDelta = -1
    smallestDeltaValues = []
    for index1, value1 in enumerate(arrayOne):
        print(f"array one - index {index1} | value: {value1}")
        for index2, value2 in enumerate(arrayTwo):
            delta = abs(value1 - value2)
            if delta <= smallestDelta or smallestDelta == -1:
                smallestDelta = delta
                smallestDeltaValues = [value1, value2]
            print(f"\tdifferences: a1[{index1}]/a2[{index2}] | {value1}/{value2} | abs diff {delta}")
    return smallestDeltaValues

array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]
smallestDelta = smallestDifference(array1, array2)
print(f"smallest difference: {smallestDelta}")