import config
import ars

def pad(p):
    rem = 16 - (len(p) % 16)
    return p + bytes([rem]) * rem

def encrypt(plaintext):
    try:
        plaintext = pad(plaintext.encode())

        a = ars.ARS(config.IV, config.KEY)
        return a.encrypt(plaintext)
    except:
        return 'Failed to encrypt text'

if __name__ == '__main__':
    import base64 as b64

    banner = r"""
               _____   _____                       _____
         /\   |  __ \ / ____|     /\        /\    / ____|
        /  \  | |__) | (___      /  \      /  \  | (___
       / /\ \ |  _  / \___ \    / /\ \    / /\ \  \___ \
      / ____ \| | \ \ ____) |  / ____ \  / ____ \ ____) |
     /_/    \_\_|  \_\_____/  /_/    \_\/_/    \_\_____/
    """

    print(banner)
    print('\n'.join([
        "",
        "Welcome to ARS Encryption as a Service!",
        "Give us a plaintext and we will encrypt it for you using our super secure key",
        "We still haven't quite worked out decryption yet though...",
        "",
        "Anyway, trust us, its fine.",
        ""
    ]))

    while True:
        try:
            inp = input('> ')
        except EOFError:
            break
        print(b64.b64encode(encrypt(inp)).decode())

    print("\nBye! (have fun decrypting those lol)")
