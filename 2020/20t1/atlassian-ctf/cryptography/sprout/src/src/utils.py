import time
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def rand_bytes(size):
    return bytearray(random.getrandbits(8) for _ in range(size))

def get_time():
    return int(time.time() * 1000)

def encrypt(content, seed=None):
    random.seed(get_time() if seed is None else seed)

    key = rand_bytes(16)
    iv  = rand_bytes(16)
    return key, iv, AES.new(key, AES.MODE_CBC, iv).encrypt(pad(content.encode(), 32))
