print("Tandem Bicycle")

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	if fastest:
		redShirtSpeeds.sort(reverse = not fastest)
		blueShirtSpeeds.sort(reverse = fastest)
	else:
		redShirtSpeeds.sort(reverse = fastest)
		blueShirtSpeeds.sort(reverse = fastest)

	print(redShirtSpeeds)
	print(blueShirtSpeeds)

	sum = 0
	for index, value in enumerate(redShirtSpeeds):
		if value > blueShirtSpeeds[index]:
			sum = sum + value
		else:
			sum = sum + blueShirtSpeeds[index]
	return sum
		

redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = False

print(f"The red shirt speeds are: {redShirtSpeeds}")
print(f"The blue shirt speeds are: {blueShirtSpeeds}")
	 
totalSpeed = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
print(f"The total speed is: {totalSpeed}")
