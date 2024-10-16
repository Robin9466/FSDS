"""### Problem Statement:

The `game()` function in a program lets a user play a game and returns the score as an integer. You need to read a file `History.txt` which is either blank or contains the previous Hi-Score. You need to write a program to update the Hi-Score whenever `game()` breaks the Hi-Score!
"""

def game():
	# Simulate game play and return score
	import random
	# Simulating a random score between 0 and 200
	score = random.randint(0, 200)
	return score # Replace with actual game logic

def update_high_score(score):
	try:
		# Read existing high score
		with open('History.txt', 'r') as file:
			high_score = file.read()
			high_score = int(high_score) if high_score else 0
	except FileNotFoundError:
		high_score = 0

	# Update if current score is higher
	if score > high_score:
		with open('History.txt', 'w') as file:
			file.write(str(score))
			print("High score updated to:", score)
	else:
		print("High score remains:", high_score)

# Main program
current_score = game()
update_high_score(current_score)

