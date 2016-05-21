# hocodeclub
Some simple scripts for use in ho code club tutorials

The first two demonstrate that programs are powerful when it comes to iterating over the same task many times, so we can use them to simulate a problem.

* monty_hall_1.py - demonstrates the probabilities in the Monty Hall problem (https://en.wikipedia.org/wiki/Monty_Hall_problem)

the basic idea is the contestant gets to pick one of three doors. Behind one door is the prize. Once they've picked, the host opens one of the unpicked doors which _doesn't_ contain the prize. The contestant is then asked whether to stick with their original pick, or switch.

This program simulates a number of trials, where the contestant can choose to stick or switch, and generates the probability of success for each strategy.

run from command line by `python manty_hall_1.py [0|1] [int]`, first argument is strategy (1 to switch), second is number of trials.

* martingale.py - simulates the Martingale betting strategy (double-down on each loss, https://en.wikipedia.org/wiki/Martingale_(betting_system))

The Martingale strategy is to bet 1, then double the stake each time you lose, so in theory the next win always recoups all your losses. The problem is that a run of losses can lead to a huge deficit.
This script simulates a number of trials, showing the accumulated winnings, and the largest deficit.

TODO plot the [Taleb](https://en.wikipedia.org/wiki/Taleb_distribution) distribution

* charts/uktop40.py - example script to scrape data from UK official charts
* charts/billboard.py - same script adapted for US billboard charts
* tube.py - a classic old riddle is 'what is the only tube station that contains none of letters of 'mackerel'?'. (http://www.robeastaway.com/blog/mackerel). this script allows you to test other phrases

