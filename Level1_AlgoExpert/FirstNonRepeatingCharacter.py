print("First Non-Repeating Character")

def firstNonRepeatingCharacter(string):
	index = 0	
	for x in string:
		print(f"character: {x} / index: {index}")
		if string.count(x) == 1:
			return index
		index = index + 1
	return -1

string = "abcabbbedda"


print(f"The sequence is: {string}")
fnrc = firstNonRepeatingCharacter(string)
print(f"The first non-repeating character is: {fnrc}")