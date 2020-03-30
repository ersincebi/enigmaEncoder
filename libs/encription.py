from libs.credentials import ROTOR, REFLECTOR, NORMALIZE, LOWERTOUPPER, LETTERLEN
from libs.rotor import rotor
from libs.reflector import reflector
from libs.revolutionTracker import revolutionTracker
from libs.plugBoard import plugBoard

class encription:
	def __init__(self):
		super().__init__()

		# call
		rotorPick = rotor(ROTOR)
		reflectorPick = reflector(REFLECTOR)
		self.revolutionStates = revolutionTracker()
		self.plugBoard = plugBoard()

		# lists
		self.rotorList = rotorPick.selection()
		self.reflectorList = reflectorPick.selection()

	def encript(self, key):
		# change rotor states on every key pressed
		self.revolutionStates.increase()
		self.revolutionStates.reset()

		# if a letter comes as lowercase, this refers it upper ascii code
		self.key = self.allwaysUpper(key)

		# ascii code to alphabet index
		self.key = NORMALIZE(self.key)

		# plug board exchange
		self.key = self.plugBoard.exchangeLetter(self.key)

		listLength = len(ROTOR)

		# fist road
		firstResult = self.road(self.key, range(listLength))

		# reflector answer
		reflectorAnswer = self.reflectorList[firstResult]

		# return road
		returnedValue = self.road(reflectorAnswer, reversed(range(listLength)))

		# again exchange letter on plugboard
		self.encripted = self.plugBoard.exchangeLetter(returnedValue)

	def road(self, letterIndex, step):
		for rotor in step:
			offset = self.revolutionStates.ringSetting[rotor]
			letterIndex = self.rotorList[rotor][0][((letterIndex + offset)%LETTERLEN)]
			letterIndex = (letterIndex - offset + LETTERLEN) % LETTERLEN

		return letterIndex

	def result(self):
		return self.encripted

	def allwaysUpper(self, key):
		try:
			return LOWERTOUPPER[key]
		except:
			return key