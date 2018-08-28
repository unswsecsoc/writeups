# Guess My Number
Medium difficulty format string challenge.    
Two writes are needed to win at the game, pwntools required  

Easy version is an option, same option but with ASLR turned off  

## Files
- flag.txt: the flag file  
- guess_my_number.c: binary compiled from this, and can be released to players  
- solver.py solver script  

## Requirements
 compiled with 32-bit, no protections (ie. -Wall -Werror off)   
 `gcc -m32 -o guess_my_number guess_my_numer.c` <-- might need to apt-get some packages to get -m32 working

## how2solve
1. name field is vulnerable to _format string_ attack
2. have to do two writes in succession
3. Overwrite the two rng value variables with the length of payload
4. enter the values you gave earlier to pass the checks
5. get flag 
