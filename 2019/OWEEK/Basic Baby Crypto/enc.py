num = "0123456789"

FLAG = "OWEEK{4iNt_CrY70_fUn}"

def encrypt(plaintext):
    enc = ""
    for i in range(0, len(plaintext)):
        if plaintext[i] in num:
            enc += chr((ord(plaintext[i]) - ord('0') + 5) % 10 + ord('0'))
        else:
            enc += plaintext[i]
    return enc.encode('rot13')

enc = encrypt(FLAG)
print enc
assert enc == "BJRRX{9vAg_PeL25_sHa}"
#print encrypt(enc) #to decode, because it's symmetric!
