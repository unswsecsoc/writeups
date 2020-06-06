import base64

def encode(plaintext, n):
    return bytes([(ch + n) % 256 for ch in plaintext])

ciphertext = base64.b64decode(input('Ciphertext: '))

prefix = b"ATLASSIAN"

rotn = prefix[0] - ciphertext[0]

print(encode(ciphertext, rotn))
