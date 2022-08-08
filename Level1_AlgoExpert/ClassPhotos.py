print("Class Photos")

def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()
	blueShirtHeights.sort()
	if redShirtHeights[0] > blueShirtHeights[0]:
		back = redShirtHeights
		front = blueShirtHeights
	else:
		back = blueShirtHeights
		front = redShirtHeights

	print(f"The red shirt heights are: {redShirtHeights}")
	print(f"The blue shirt heights are: {blueShirtHeights}")
	print(f"The back row is: {back}")	
	
	for index, value in enumerate(back):
		if back[index] <= front[index]:
			print(f"{back[index]} vs {front[index]}")
			return False
	return True

redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
print(f"The red shirt heights are: {redShirtHeights}")
print(f"The blue shirt heights are: {blueShirtHeights}")
print("--------------------")

response = classPhotos(redShirtHeights, blueShirtHeights)
print(f"{response}")