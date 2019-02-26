from lantern.modules import vigenere
#from lantern.fitness import ChiSquared
#from lantern.fitness import PatternMatch
from itertools import product

import sys
import string
import re

ciphertext = "}tfequwkpeagims{xmow"

#fitness = ChiSquared(frequency.english.unigrams)
#decryptions = vigenere.crack(ciphertext.upper(), fitness)

#fitness = PatternMatch("}.*{galf")
#decryptions = vigenere.crack(ciphertext, fitness, max_key_period=3)


## BEST FORCE ##
for i in range(1,len(ciphertext)): #blooper: starting at zero and getting index out of range error
    #print(i)
    for fuc in product(string.ascii_lowercase, repeat = i):
        # need to explicitly include the name 'repeat'
        key = ''.join(fuc)
        decryptions = vigenere.decrypt(key, ciphertext)
        pattern = re.compile("}.*{galf")                                         
        #print("trying key "+key)
        if pattern.search(decryptions) is not None:
            print("Key: "+key)
            print("Plaintext: "+decryptions)
            sys.exit() 
            # there's more than one key that will produce a match, but the solution happens to be the first

# NOTE: The encryption steps were:
# 1. reverse string
# 2. apply vigenere
# but since the length of the text (minus the {}) is cleanly divisible by the key length,
# you can also reverse the ciphertext before trying to crack the vigenere cipher, the key
# will simply be backwards

# Also, a much nicer solution would've been to use vigenere.crack with PatternMatch as
# the fitness function. However, they don't seem to work together, so this is the next
# best thing you can do

