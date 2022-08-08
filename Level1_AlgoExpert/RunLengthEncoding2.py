print("Run Length Encoding")

def runLengthEncoding(string):	
	encodedText = ""
	while len(string) > 0:
		count = 0
		while count < 9 and count < len(string) and string[count] == string[0]:	
			count = count + 1
		encodedText = encodedText + str(count)
		encodedText = encodedText + string[0]
		string = string[count:]
	return encodedText


message = "AAAAAAAAAAAAABBCCCCDD"
print(f"The message is: {message}")
encodedText = runLengthEncoding(message)
print(f"The cipher text is: {encodedText}")