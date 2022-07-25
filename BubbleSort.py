print("Bubble Sort")

def bubbleSort(array):
	n = len(array)
	for x in array:
		count = 1 
		while count < n:
			if array[count] < array[count - 1]:
				swapValue = array[count]
				array[count] = array[count - 1]
				array[count - 1] = swapValue
			count = count + 1
	return array

sortMe = [8, 5, 2, 9, 5, 6, 3]

print(f"The unsorted array is: {sortMe}")
sorted = bubbleSort(sortMe)
print(f"The sorted array is: {sorted}")