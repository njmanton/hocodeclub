# import random
import random, sys

# counting variables
wins = 0  # number of wins
losses = 0 # number of losses

# get choice of switch from command line if present, otherwise 1 (switch). argv[0] is always filename
switch = int(sys.argv[1]) if len(sys.argv) >= 2 else 1

# get number of trials from command line if present, otherwise 1M
trials = int(sys.argv[2]) if len(sys.argv) >= 3 else 1000000


for _ in range(trials):
	
	# randomly set the prize
	prize = random.randint(1,3)

	# randomly pick a door (or rather, set the random door to be door 1)
	picked = 1 #random.randint(1,3)

	# open a random door
	# BUT, can't open the selected door, OR the prize door
	opened = random.randint(2,3)
	while opened == prize:
		opened = random.randint(2,3)

	if switch == 1:
		# if the strategy is to switch:
		# pick the door which isn't the original pick (1) and not the opened door
		picked = 5 - opened
		# this calculation works because if opened is 3, we want door 2, and vice-versa
		# so 5 - opened will give the right result either way

	if picked == prize:
		# win
		wins += 1
	else:
		# lose
		losses += 1

print (trials, "trials\n")
print ("with switch =", switch, "\n")
print ("wins:", wins)
print ("losses:", losses)
