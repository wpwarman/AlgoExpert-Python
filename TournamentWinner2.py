def tournamentWinner(competitions, results):
	teams = {}
	for x in competitions:
		index = competitions.index(x)
		if results[index] == 1:		
			winner = x[0]
		else:
			winner = x[1]
    
		# Update the scores dictionary	
		if winner in teams:
			teams[winner] = teams[winner] + 3
		else:
			teams[winner] = 3
		
		returnValue = max(teams, key= lambda x: teams[x])
		
	return returnValue

competitions = [["HTML", "Java"],["Java", "Python"],["Python", "HTML"]]
results = [0, 1, 1]

winner = tournamentWinner(competitions, results)
print(f"The winner is: {winner}")
