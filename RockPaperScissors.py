#Goals: 
# 1. Ask the player if they pick rock paper or scissors - COMPLETED 
# 2. Have the computer choose its move 
	#2A How will the computer choose its move?
		# Random integer and then assign those integers to string values? 
		# Computer will select randomly. However when comparing it against each other,
		# be sure to compare the string values instead of the numerical values
# 3. Compare the choices and decide who wins 
	#3A. Do a logic dump?
		# if compchoice "rock": 
			# user wins 
		# else: 
			# compuer wins 
# 4. Print the results 

import random 

def ask_user():
	x = ["rock", "paper", "scissors"]
	while True:
		response = raw_input("Rock, Paper, or Scissors?: ")
		response = response.lower()
		if response in x:
			break
	return response
	
def computer(): 
	comp_dec = ""
	z = (random.randrange(0, 3))
	if z == 0:
		comp_dec = "Rock"
	elif z == 1: 
		comp_dec = "Paper"
	else:
		comp_dec = "Scissors"
	return comp_dec.lower()

def comparison(response): 
	comp = ""
	computer_selection = computer()
	print "You have picked %s, the computer has picked %s " % (response, computer_selection)
	if (computer_selection == 'rock') and (response == "rock"):
			comp = "Its a Tie!1"
	elif (computer_selection == 'scissors') and (response == "scissors"):
			comp = "Its a Tie!2"
	elif (computer_selection == 'paper') and (response == "paper"):
			comp = "Its a Tie!3"
	elif (computer_selection == 'scissors') and (response == 'rock'):
			comp = "You Win!1"
	elif (computer_selection == 'scissors') and (response == 'paper'):
			comp = "The Computer Wins!1"
	elif (computer_selection == 'rock') and (response == 'paper'):
			comp = "You Win!2"
	elif (computer_selection == 'rock') and (response == 'scissors'):
			comp = "The Computer Wins!2"
	elif (computer_selection == 'paper') and (response == 'scissors'):
			comp = "You Win!3"
	else:
		comp = "The Computer Wins!3"
	return comp

# set ask_user to variable (i.e. r = ask_user)
# select rock // paper // scissors after setting variable 
# now call comparison function with the variable that was set to ask_user (i.e. comparison(r))
# keep calling comparison(r) to play number of times