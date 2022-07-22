print("Caesar Cyphir Encyrptor\n")

def CaesarCipherEncryptor(message):
	pass
	
	
message = "ahelloz"
offset = 12
completedCipher = ""

print(f"The message is: {message}\n")
for x in message:
	print(f"The ACSII value of {x} is: {ord(x)}")
	ccv = (ord(x) + offset - 97)%26
	newChar = chr(ccv + 97)
	completedCipher = completedCipher + newChar
	print(f"The Caesar Cipher of {x} wth offset of {offset} is {newChar}")
	print("--------------------------")

print(f"The complete encrypted text is: {completedCipher}")