#plain = "Hello and welcome to my lovely simple vigenere challenge! Isn't this fun? Anyway, here is your beautiful flag OWEEK{jUst_NeEd_mY_k3y}"

plain = "HELLO AND WELCOME TO MY LOVELY SIMPLE VIGENERE CHALLENGE! ISN'T THIS FUN? ANYWAY, HERE IS YOUR BEAUTIFUL FLAG OWEEK{JU5T_N3ED_MY_K3Y}"
key = "MELOVEHACKING"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(key, plaintext):
    repeat_key = ""
    i = 0
    for letter in plaintext:
        if letter in alphabet:
            repeat_key += key[i % len(key)]
            i += 1
        else:
            repeat_key += ' '
    
    ciphertext = ""
    for k, p in zip(repeat_key, plaintext):
        shift = p
        if shift in alphabet:
            shift = chr((ord(p) + ord(k)) % len(alphabet) + ord('A'))
        ciphertext += shift
    return ciphertext

def decrypt(key, ciphertext):
    repeated_key = ""
    j = 0
    for i in range(len(ciphertext)):
        if ciphertext[i] in alphabet:
            repeated_key += key[j % len(key)]
            j += 1
        else:
            repeated_key += ' '
    
    plaintext = ""
    for key_i, letter_i in zip(repeated_key, ciphertext):
        # Implement the shifting logic
        shifted_letter = letter_i
        if letter_i in alphabet:
            shifted_letter = chr((ord(letter_i) - ord(key_i)) % len(alphabet) + ord("A"))
        plaintext += shifted_letter

    return plaintext

cipher = encrypt(key, plain)
print cipher
#print decrypt(key, cipher) #to decode
