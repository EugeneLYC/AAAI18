import random
import math
import sys

class Blag:
	def __init__(self, m, f, prob_0, Actionset, epsilon):
		self.m = m
		self.f = f
		self.prob_0 = prob_0
		self.Actionset = Actionset
		self.epsilon = epsilon

		self.ActionPool = []
		self.ASG_reward = dict()
		self.ASG_num = dict()
		self.blag = [0]
		self.infoLoss = [0]

		for actionId in range(len(self.Actionset)):
			self.ActionPool.append(actionId)
			self.ASG_reward[actionId] = 0
			self.ASG_num[actionId] = 1


	def getBlag(self):
		return self.blag

	def getInfoLoss(self):
		return self.infoLoss

	#detecting whether vector aciton1 and action2 is conflicting
	def conflict(self, action1, action2):
		for itr in range(self.m):
			if action1[itr]*action2[itr] < 0:
				return True
			if self.prob_0[itr]+action1[itr]+action2[itr] < 0 or self.prob_0[itr]+action1[itr]+action2[itr] > 1:
				return True
		return False


	def exploration(self):
		selected = []
		action = [0 for i in range(self.m)]
		startid = random.choice(self.ActionPool)
		for itr in range(self.m):
			action[itr] += self.Actionset[startid][itr]
		for actionId in range(startid-1,0,-1):
			if not self.conflict(action, self.Actionset[actionId]) and actionId in self.ActionPool:
				selected.append(actionId)
				for itr in range(self.m):
					action[itr] += self.Actionset[actionId][itr]
		for actionId in range(startid+1,len(self.Actionset)):
			if not self.conflict(action, self.Actionset[actionId]) and actionId in self.ActionPool:
				selected.append(actionId)
				for itr in range(self.m):
					action[itr] += self.Actionset[actionId][itr]
		return selected

	def exploitation(self):
		currentReward = sorted(self.ASG_reward.items(), key=lambda d: d[1])
		selected = []
		action = [0 for i in range(self.m)]
		for tupleVer in currentReward:
			if not self.conflict(action, self.Actionset[tupleVer[0]]) and tupleVer[0] in self.ActionPool\
																		 and self.ASG_reward[tupleVer[0]] >= 0:
				selected.append(tupleVer[0])
				#print(self.ASG_reward[tupleVer[0]])
				for itr in range(self.m):
					action[itr] += self.Actionset[tupleVer[0]][itr]
		return selected

	def bandit(self, Time):
		for time in range(1, Time+1):
			#self.epsilon /= (time**0.25)
			sum = 0
			var = random.uniform(0,0.001) - random.uniform(0,0.001)

			if random.uniform(0,1) < self.epsilon:
				self.epsilon /= 2
				combination = self.exploration()
			else:
				combination = self.exploitation()

			for actionId in combination:
				self.ASG_num[actionId] += 1
				for i in range(self.m):
					sum += self.f[i]*(self.Actionset[actionId][i] + var)
			self.blag.append(sum)

			for actionId in combination:
				re_node = 0
				for i in range(self.m):
					re_node += self.f[i]*(self.Actionset[actionId][i]) + var
				self.ASG_reward[actionId] = ((time-1)*self.ASG_reward[actionId] + re_node)/time

