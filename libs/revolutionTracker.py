from libs.credentials import STARTSTATES, ALPHABET

class revolutionTracker:
	def __init__(self):
		super().__init__()
		self.max_state = len(ALPHABET)-1
		self.startStates = STARTSTATES
		self.state = 1

	def increase(self):
		if self.state == len(self.startStates):
			return 0
		if self.startStates[self.state-1] == self.max_state:
			self.startStates[self.state] += 1
			self.startStates[self.state-1] = 1
			self.state += 1
			return self.increase()
		else:
			self.startStates[0] += 1

	def reset(self):
		self.state = 1