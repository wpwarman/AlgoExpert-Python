print("Find the Three Largest Numbers")

def findThreeLargestNumbers(array):
	returnValue = []
	for x in range(1,4):
		maxValue = max(array)
		array.remove(maxValue)
		returnValue.insert(0, maxValue)
	return returnValue
	
array = [-5, 7, 19, 19, 23, 4, 8]
print(f"The array is: {array}")
threeLargest = findThreeLargestNumbers(array)
print(f"The three largest values are: {threeLargest}")
	