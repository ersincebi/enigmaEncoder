from msvcrt import kbhit, getch
from libs.encription import encription
from libs.credentials import ALPHABET

def main():
	encript = encription()
	while True:
		if kbhit():
			encript.encript(ord(getch()))
			print(ALPHABET[encript.result()])

if __name__ == '__main__':
	main()
