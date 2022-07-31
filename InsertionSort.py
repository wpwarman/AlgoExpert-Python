print("Insertion Sort")

def insertionSort(array):
	for x in range(0, len(array)):
		y = x
		while y > 0:
			y = y - 1
			if array[y] > array[y + 1]:
				temp = array[y + 1]
				array[y + 1] = array[y]
				array[y] = temp
	return array


sortMe = [8, 5, 2, 9, 5, 6, 3]
print(f"The unsorted array is: {sortMe}")
sorted = insertionSort(sortMe)
print(f"The sorted array is: {sorted}")