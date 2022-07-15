print("Two Number Sum")

def twoNumberSum(array, targetSum):
    index = 0
    while index < len(array):
        findMe = targetSum - array[index]
        if findMe in array and array[index] != findMe:
            return [array[index], findMe]
        index = index + 1
    return []

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(f"This array is: {array}")
print(f"The target sum is: {targetSum}")

test = twoNumberSum(array, targetSum)
print(f"The test array is: {test}")