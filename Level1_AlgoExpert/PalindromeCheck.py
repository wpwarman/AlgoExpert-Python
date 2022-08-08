print("Palindrome Check")

def isPalindrome(string):
	string = string.lower()
	y = len(string)
	for x in range(0,y):
		y = y - 1
		if string[x] != string[y]:
			return False
	return True
	
checkMe = "tacoCat"
print(f"Checking: {checkMe}")
if isPalindrome(checkMe):
	print(f"{checkMe} IS a palindrome!")
else:
	print(f"{checkMe} IS NOT a palindrome!")
	