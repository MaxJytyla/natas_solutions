import collections
import sys
import string

def main(ciphertext,freqstr="ETAOINSHRDLCUMWFGYPBVKJXQZ"):
	raw_cipher = ''.join(ciphertext.strip().split())
	freq = dict(collections.Counter(raw_cipher))
	cipher_freq = sorted([[x,freq[x]] for x in freq.keys()], key=lambda x: x[1], reverse=True)
	cipher_freq_str = ''.join([x[0] for x in cipher_freq])
	print('Frequency of letters in cipher_text (Not including spaces or alphanumberic characters):')
	for x in cipher_freq:
		print(x[0], f'{100*x[1]/len(raw_cipher):.3f}%')
	decode_str = ''.join([freqstr[cipher_freq_str.index(x)] if x.isalpha() else x for x in ciphertext])
	print()
	print('Text after being decoded with frequency string.')
	print(decode_str)

if __name__=="__main__":
	if len(sys.argv) == 2:
		ciphertext = open(sys.argv[1], 'r').read()
		main(ciphertext)
	elif len(sys.argv) == 3:
		ciphertext = open(sys.argv[1], 'r').read()
		main(ciphertext, sys.argv[2])
	else:
		print('Usage: python3 freq_analysis.py [cipher file] [frequency string (default ETAOINSHRDLCUMWFGYPBVKJXQZ)]')