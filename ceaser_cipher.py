import sys
LOWER_ORD = 97
UPPER_ORD = 65


def main(pos, ciphertext):
	plaintext =  ''
	for x in ciphertext:
		if not x.isalpha():
			plaintext += x
			continue
		elif x.isupper():
			plaintext += chr(((ord(x) - UPPER_ORD + pos)%26) + UPPER_ORD)
		elif x.islower():
			plaintext += chr(((ord(x) - LOWER_ORD + pos)%26) + LOWER_ORD)
	print(plaintext)

if __name__=="__main__":
	try:
		if len(sys.argv) != 3:
			raise ValueError
		pos = int(sys.argv[1])
		ciphertext = sys.argv[2]
	except ValueError as e:
		print("ceaser_cipher.py usage: python3 ceaser_cipher.py [pos to move characters: int] [alphachar string to be decoded.]")
		quit()
	
	main(pos, ciphertext)