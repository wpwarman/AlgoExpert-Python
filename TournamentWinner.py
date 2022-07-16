print("Tournament Winner")

#	INPUT
#	format of competitions array: [[home, away], [home, away]...]
#	format of record array: [0 or 1, 0 or 1,...]
#		where 0 = hometeam loss and 1 = hometeam win 

# competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
# record = [0, 0, 1]
competitions = [["HTML", "Java"],["Java", "Python"],["Python", "HTML"]]
record = [0, 1, 1]
teams = {}

for x in competitions:
	
	# Determine the winning team based on the record
	index = competitions.index(x)
	if record[index] == 1:		
		winner = x[0]
	else:
		winner = x[1]

	# Update the scores dictionary	
	if winner in teams:
		teams[winner] = teams[winner] + 3
	else:
		teams[winner] = 3
	
# Print the results	
print("The final scores are: ", teams)
print("NOTE: Teams with a score of 0 points are\nnot included because they have no chance of winning")




