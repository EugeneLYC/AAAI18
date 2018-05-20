import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from blag import Blag
from linucb import Linucb
from linear import Linear
import random
import sys


m = int(sys.argv[1])
epsilon = 0.1
f = []
prob_0 = []
for i in range(m):
	f.append(random.randint(1,1000))
	prob_0.append(random.uniform(0,1))

Actionset = []

def initial():
	#Filling the ActionSet
	while True:
		action = [0 for i in range(m)]
		for itr in range(m-1):
			for itr2 in range(itr+1,m):
				probability = random.uniform(0,0.5)
				action[itr] = probability
				action[itr2] = -probability
				Actionset.append(action)
				action = [0 for i in range(m)]
				action[itr] = probability
				action[itr2] = -probability
				Actionset.append(action)
				action = [0 for i in range(m)]
		break

initial()

TIME = int(sys.argv[2])

ucb_trial = Linucb(m, f, prob_0, Actionset, 0)
ucb_trial.bandit(TIME)
ucb_plot = ucb_trial.getLinucb()/500/int(sys.argv[1])

blag_trial = Blag(m, f, prob_0, Actionset, 0.1)
blag_trial.bandit(TIME)
blag_plot = blag_trial.getBlag()/500/int(sys.argv[1])


outfile = open('comparison.txt','w+')
outfile.write('\nExperiment setting: m='+sys.argv[1]+' TIME='+sys.argv[2]+':\n')
outfile.write('BLAG: '+sys(blag_plot))
outfile.write('UCB: '+sys(ucb_plot))
outfile.close()
