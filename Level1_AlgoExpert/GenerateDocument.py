print("Generate Document")

def generateDocument(characters, document):	
	for x in document:
		if x in characters:
			print(f"I found {x}")
			characters = characters.replace(x, '', 1)
			print(characters)
		else:
			return False
	return True

characters = "abcabc"
document = "aabbcc"

print(f"The characters are: {characters}")
print(f"The document requested is: {document}")
	 
if generateDocument(characters, document):
    print("The document CAN be generated")
else:
    print("The document CANNOT be generated")