from libs.credentials import RINGSETTING, RINGPOSITION

class revolutionTracker:
	def __init__(self):
		super().__init__()
		self.max_state = RINGPOSITION
		self.ringSetting = RINGSETTING
		self.state = 1

	def increase(self):
		if self.state == len(self.ringSetting):
			return 0
		if self.ringSetting[self.state-1] == self.max_state[self.state-1]:
			self.ringSetting[self.state] += 1
			self.ringSetting[self.state-1] = 1
			self.state += 1
			return self.increase()
		else:
			self.ringSetting[0] += 1

	def reset(self):
		self.state = 1