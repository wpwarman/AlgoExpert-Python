print("Selection Sort")

def selectionSort(array):
	for bottomIndex in range(0,len(array)):
		lowestValue = array[bottomIndex]
		lowestIndex = bottomIndex
		
		for index in range(bottomIndex, len(array)):
			x = array[index]			
			if x < lowestValue:
				lowestValue = x
				lowestIndex = index
			
		swapValue = array[bottomIndex]
		array[bottomIndex] = lowestValue
		array[lowestIndex] = swapValue
	return array

sortMe = [8, 5, 2, 9, 5, 6, 3]

print(f"The unsorted array is: {sortMe}")
sorted = selectionSort(sortMe)
print(f"The sorted array is: {sorted}")