import base64

def encode(plaintext, n):
    return bytes([(ch + n) % 256 for ch in plaintext])

if __name__ == '__main__':
    import sys
    print(base64.b64encode(encode(open(sys.argv[1], 'rb').read(), int(sys.argv[2]))).decode())
