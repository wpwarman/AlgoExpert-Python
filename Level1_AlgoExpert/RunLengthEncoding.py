print("Run Length Encoding")

def runLengthEncoding(string):	
	message = list(string)

	encodedText = []
	
	while len(message) > 0:
		count = 0
		value = message[0]
		while count < 9 and count < len(message) and message[count] == message[0]:
			print(f"count: {count} / value: {value} / message[value]: {message[count]}")	
			count = count + 1
		encodedText.append(count)
		encodedText.append(value)
		del message[:count]
		print(f"message: {message}")
		print(f"encodedText: {encodedText}")
		text = "".join(map(str,encodedText))
	return text


message = "AAAAAAAAAAAAABBCCCCDD"
print(f"The message is: {message}")
encodedText = runLengthEncoding(message)
print(f"The cipher text is: {encodedText}")