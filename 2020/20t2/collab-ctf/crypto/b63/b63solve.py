# same alphabet as base 64
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

with open('b63.txt', 'r') as f:
	for line in f:
		for word in line.split():
			num = alphabet.index(word[0])*63 + alphabet.index(word[1])
			print(chr(num), end = '')
print()
