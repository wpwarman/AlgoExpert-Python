print("Binary Search")

def binarySearch(array, target):
	
	# set up
	low = 0
	mid = -1
	high = len(array) - 1

	while True:
		
		# if the midpoint doesn't change, 
		# then we're repeating ourselves and
		# the target is not in the array. So 
		# keeep track of the old midpoint.
		
		oldMid = mid
		mid = int((high+low)/2)
		
		# don't do work if we don't have to
		if oldMid == mid:		# see above
			return -1
		if target == array[low]:
			return low
		if target == array[high]:	
			return high		
		if target == array[mid]:
			return mid
						
		# adjust the bounds and try again
		if target > array[mid]:
			low = mid
		elif target < array[mid]:
			high = mid
				
	# we should never get here
	return -1

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 25

print(f"The array is: {array}")
print(f"The target is: {target}")
	 
index = binarySearch(array, target)
print(f"index:{index}")
if index >= 0:
	print(f"The target is at index: {index}")
else:
	print("The target could not be found")
