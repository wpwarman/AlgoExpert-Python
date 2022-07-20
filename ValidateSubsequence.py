def isValidSubsequence(array, sequence):
    for x in sequence:
        if x in array:
            i = array.index(x)
        else:
            return False
        array = array[i + 1:len(array)]
    return True


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(f"The array is {array}")
print(f"The subsequence is {sequence}")
	 
if isValidSubsequence(array, sequence):
    print("The subsequence is valid")
else:
    print("The subsequence is not valid")