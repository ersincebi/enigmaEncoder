from libs.credentials import PLUGCONNECTIONS
import random as rnd

class plugBoard:
	def __init__(self):
		super().__init__()
		self.sequence = PLUGCONNECTIONS
		if self.sequence is None:
			self.sequence = self.setSequence()

	def exchangeLetter(self, letter):
		for plugged in self.sequence:
			if letter in plugged:
				pluggedValue = plugged[1-plugged.index(letter)]
				break
			else:
				pluggedValue = letter
		return pluggedValue

	def setSequence(self):
		lst = list(range(1,27))
		seen = set()
		choices = [0,0]
		plugSequence = []
		index = 0
		while True:
			x = rnd.randint(1,25)
			y = rnd.randint(1,25)
			if x not in seen and y not in seen and x != y:
				seen.add(x)
				seen.add(y)
				plugSequence.append([lst[y], lst[x]])
				index +=1
				if index == 10:
					break
		print("Plug Board Sequence: ",plugSequence)