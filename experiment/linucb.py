import random
import math
import sys

class Linucb:
	def __init__(self, m, f, prob_0, Actionset, init_est):
		self.m = m
		self.f = f
		self.prob_0 = prob_0
		self.Actionset = Actionset

		self.ActionPool = []
		self.ASG_reward = dict()
		self.ASG_num = dict()
		self.Combination = dict()
		self.linucb = [0]
		self.infoLoss = [0]

		for actionId in range(len(self.Actionset)):
			self.ActionPool.append(actionId)
			self.ASG_reward[actionId] = init_est
			self.ASG_num[actionId] = 1



	#detecting whether vector aciton1 and action2 is conflicting

	def getLinucb(self):
		return self.linucb

	def getInfoLoss(self):
		return self.infoLoss


	def conflict(self, action1, action2):
		for itr in range(self.m):
			if action1[itr]*action2[itr] < 0:
				return True
			if self.prob_0[itr]+action1[itr]+action2[itr] < 0 or self.prob_0[itr]+action1[itr]+action2[itr] > 1:
				return True
		return False


	def ucb(self, time):
		for actionId in range(len(self.Actionset)):
			self.Combination[actionId] = self.ASG_reward[actionId] + math.sqrt(math.log(time)/self.ASG_num[actionId])
		currentReward = sorted(self.Combination.items(), key=lambda d: d[1])
		selected = []
		action = [0 for i in range(self.m)]
		for tupleVer in currentReward:
			if not self.conflict(action, self.Actionset[tupleVer[0]]) and tupleVer[0] in self.ActionPool:
				selected.append(tupleVer[0])
				for itr in range(self.m):
					action[itr] += self.Actionset[tupleVer[0]][itr]
		return selected


	def bandit(self, Time):
		for time in range(1, Time+1):
			sum = 0
			var = random.uniform(0,0.001) - random.uniform(0,0.001)

			combination = self.ucb(time)

			for actionId in combination:
				self.ASG_num[actionId] += 1
				for i in range(self.m):
					sum = sum + self.f[i]*(self.Actionset[actionId][i]) + var
			re = sum/(len(combination)+1)
			self.linucb.append(re)
			self.infoLoss.append(sum)

			for actionId in combination:
				re_node = 0
				for i in range(self.m):
					re_node += self.f[i]*(self.Actionset[actionId][i]) + var
				self.ASG_reward[actionId] = ((time-1)*self.ASG_reward[actionId] + re_node)/time

			#prune(time)
