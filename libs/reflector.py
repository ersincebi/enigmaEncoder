class reflector(object):
	def __init__(self, arg):
		self.arg = arg
		self.reflectors = {
			# YRUHQSLDPXNGOKMIEBFZCWVJAT
			'B': {1: 25, 2: 18, 3: 21, 4: 8, 5: 17, 6: 19, 7: 12, 8: 4, 9: 16, 10: 24, 11: 14, 12: 7, 13: 15, 14: 11, 15: 13, 16: 9, 17: 5, 18: 2, 19: 6, 20: 26, 21: 3, 22: 23, 23: 22, 24: 10, 25: 1, 26: 20}
			# FVPJIAOYEDRZXWGCTKUQSBNMHL
			,'C': {1: 6, 2: 22, 3: 16, 4: 10, 5: 9, 6: 1, 7: 15, 8: 25, 9: 5, 10: 4, 11: 18, 12: 26, 13: 24, 14: 23, 15: 7, 16: 3, 17: 20, 18: 11, 19: 21, 20: 17, 21: 19, 22: 2, 23: 14, 24: 13, 25: 8, 26: 12}
			# ENKQAUYWJICOPBLMDXZVFTHRGS
			,'BT': {1: 5, 2: 14, 3: 11, 4: 17, 5: 1, 6: 21, 7: 25, 8: 23, 9: 10, 10: 9, 11: 3, 12: 15, 13: 16, 14: 2, 15: 12, 16: 13, 17: 4, 18: 24, 19: 26, 20: 22, 21: 6, 22: 20, 23: 8, 24: 18, 25: 7, 26: 19}
			# RDOBJNTKVEHMLFCWZAXGYIPSUQ
			,'CT': {1: 18, 2: 4, 3: 15, 4: 2, 5: 10, 6: 14, 7: 20, 8: 11, 9: 22, 10: 5, 11: 8, 12: 13, 13: 12, 14: 6, 15: 3, 16: 23, 17: 26, 18: 1, 19: 24, 20: 7, 21: 25, 22: 9, 23: 16, 24: 19, 25: 21, 26: 17}
		}


	def selection(self):
		return self.reflectors[self.arg]