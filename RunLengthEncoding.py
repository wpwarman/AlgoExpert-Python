print("Run Length Encoding")

def runLengthEncoding(string):
	encodedText = []
	count = 0
	value = string[0]
	print(f"encodedText: {encodedText} / count: {count} / string {string}")
	while count < 9 and len(string) > 0:
		print("-- in while") 
		if string[0] == string[count]:
			print("-- in if")
			count = count + 1		
		else:
			print("-- in else")
			encodedText.append(count)
			encodedText.append(value)
			string = string.replace(value, "", count)
			print (f"The shortened string is: {string}")
		#runLengthEncoding(string)
	return encodedText

message = "AAAAAAAAAAAAABBCCCCDD"

print(f"The message is: {message}")
encodedText = runLengthEncoding(message)
print(f"The cipher text is: {encodedText}")