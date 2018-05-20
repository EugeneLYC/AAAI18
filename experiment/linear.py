import random
import math

class Linear:
	def __init__(self, m, f, prob):
		self.m = m
		self.f = f
		#self.prob_0 = prob_0
		self.prob = prob
		self.infoLoss = [0]

	def getInfoLoss(self):
		return self.infoLoss

	def bandit(self, Time):
		for time in range(1, Time+1):
			sum = 0
			var = random.uniform(0,0.01) - random.uniform(0,0.01)

			for i in range(self.m):
				sum += min(1,(self.prob+var)*math.log(time))*self.f[i]

			self.infoLoss.append(sum)
