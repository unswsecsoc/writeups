import base64 as b64
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def rand_bytes(size):
    return bytearray(random.getrandbits(8) for _ in range(size))

def decrypt(content, seed=None):
    random.seed(seed)
    content = b64.b64decode(content)

    key = rand_bytes(16)
    iv  = rand_bytes(16)
    return unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(content), 32).decode()

if __name__ == '__main__':
    message = input('Message (b64): ')
    time    = input('Time (unix): ')

    print(decrypt(message, seed=int(time)))
