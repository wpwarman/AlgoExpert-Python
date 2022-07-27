print("Binary Search")

def binarySearch(array, target):	
	return -1

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

print(f"The array is: {array}")
print(f"The target is: {target}")
	 
index = binarySearch(array, target)

if index >= 0:
	print(f"The target is at index: {index}")
else:
	print("The target could not be found")
