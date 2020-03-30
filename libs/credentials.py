ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERLEN = len(ALPHABET)-1

# rotor selection could be 1, 2, 3, 4, 5
ROTOR = [2, 5, 3]

# each state could be between 1 to 26
RINGSETTING = [1, 2, 3]

# each state could be between 1 to 26
RINGPOSITION = [10, 13, 20]

# reflector selection could be B, C, BT, CT
REFLECTOR = 'B'

# plub board patern
PLUGCONNECTIONS = [[16, 3], [9, 26], [7, 4], [5, 10], [23, 12], [17, 25], [19, 22], [13, 11], [20, 21], [6, 24]]

LOWERTOUPPER = {97: 65, 98: 66, 99: 67, 100: 68, 101: 69, 102: 70, 103: 71, 104: 72, 105: 73, 106: 74, 107: 75, 108: 76, 109: 77, 110: 78, 111: 79, 112: 80, 113: 81, 114: 82, 115: 83, 116: 84, 117: 85, 118: 86, 119: 87, 120: 88, 121: 89, 122: 90}

NORMALIZE = lambda letter: letter - 64
