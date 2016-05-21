# TODO
# plot the cumulative balance over time to show the taleb distribution

# get the random package
import random

trials = 1000 # number of hands to play
odds = 0.474 # chance of winning a hand (0.474 is the probability of choosing red/black in roulette)
payout = 2 # payout
stake = 1 # initial stake
prev = None # what was the previous bet
balance = 1 # balance
max_deficit = 0 # what's the biggest loss we get to?

for _ in range(trials):

    # perform a trial
    if random.random() <= odds:
        #win
        balance += stake
        stake = 1
    else:
        #lose
        balance -= stake
        max_deficit = min(max_deficit, balance)
        stake *= 2

print ("After", trials, "trials:")
print ("Winnings:", balance)
print ("Max deficit:", max_deficit)
