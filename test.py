import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from blag import Blag
from linucb import Linucb
from linear import Linear
import random


m = 10
epsilon = 0.1
f = []
prob_0 = []
for i in range(m):
	f.append(random.randint(1000,2000))
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

TIME = 1000

'''
ucb_trial = Linucb(m, f, prob_0, Actionset, 0)
ucb_trial.bandit(TIME)
ucb_plot = ucb_trial.getLinucb()
ucb_display = [0]
'''

blag_trial = Blag(m, f, prob_0, Actionset, 0.1)
blag_trial.bandit(TIME)
blag_plot = blag_trial.getInfoLoss()
blag_display = [0]

linear_trial = Linear(m, f, 0.01)
linear_trial.bandit(TIME)
linear_plot = linear_trial.getInfoLoss()
linear_display = [0]

timeline = [0]

interval = 100
for i in range(1,int(TIME/interval)):

	average = sum(blag_plot[(i-1)*interval:i*interval])/interval
	blag_display.append(average)

	#average = sum(ucb_plot[(i-1)*interval:i*interval])/interval
	#ucb_display.append(average)

	average = sum(linear_plot[(i-1)*interval:i*interval])/interval
	linear_display.append(average)

	timeline.append(i*interval)

norm = max(linear_display)
for i in range(len(linear_display)):
	linear_display[i] /= norm
	blag_display[i] /= norm
fig,ax = plt.subplots(figsize=(12,7))
ax.set_xlabel('Round',fontsize=25, FontWeight='bold')  
ax.set_ylabel('Normalized Data Loss',fontsize=25, FontWeight='bold')
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
#xlim=(0,int(sys.argv[2]))
#ax.plot(timeline, original_display, 'xk-', markerfacecolor='None', markeredgewidth=3, markersize=22 ,label="original", linewidth=5)
#ax.plot(timeline, bag_nonprune_display, 'sk-', markerfacecolor='None', markeredgewidth=3, markersize=22 ,label="no prune", linewidth=5)   
ax.plot(timeline, linear_display, '^k-', markerfacecolor='None', markeredgewidth=3, markersize=22 ,label="Decrease with time", linewidth=5)   
ax.plot(timeline, blag_display, 'or-', markerfacecolor='None', markeredgewidth=3, markersize=22 ,label="BLAG", linewidth=5)
ax.grid(True)
#plt.figure(figsize=(20,10),dpi=100)
ax.legend(loc=2, borderaxespad=0.,fontsize=25)  
fig.savefig('test.png')
