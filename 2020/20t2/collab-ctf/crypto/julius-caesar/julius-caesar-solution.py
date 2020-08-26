'''
CSESoc x SecSoc 2020 CTF
Decryption function for 'Julius Caesar' challenge
Ada Luong, July 2020
'''

def decrypt(text, shift1, shift2):
    decrypted = ''
    count = 0
    for char in text.upper():
        if char.isalpha():
            if count % 2 == 0:
                decrypted += chr(((ord(char) - ord('A') + shift1) % 26) + ord('A'))
            else:
                decrypted += chr(((ord(char) - ord('A') + shift2) % 26) + ord('A'))
        else:
            decrypted += char
        
        count+=1

    return decrypted

text = input('Text: ')
shift1 = 26 - 15
shift2 = 26 - 3
decrypted_text = decrypt(text, shift1, shift2)

print(decrypted_text)
