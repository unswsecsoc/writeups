# Title
Escape the Matrix


## Description (hidden from players)
ciphertext encoded with repeated XOR-ing.


## Flavour (for players to see)
Neo found himself trapped in a Matrix made of 1's and 0's... time is running out and only you can save him...


## Hints
Did you use your logic?


## Running (how to run, if required)
Just give them the cipher text - matrix.txt :)


## Walkthrough
* you are going to want to write a script for this
* first notice that the first byte (8 bits) of the binary string is "f" (first letter of the flag) if converted to ascii
* from there take the "f" byte and XOR with the rest of the string -> resulting in string2
* now take the first byte of string2 (which is the next letter in the flag ascii "l") and XOR again to the rest of the string after "l" -> string3
* the string will get smaller, repeat until the last byte is decoded.
* solution in C can be found in matrixSolver.c


## Flag
flag{didyouautomatethis?}
