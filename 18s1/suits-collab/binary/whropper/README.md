# Whropper
Special thanks to Keiran who shared this challenge with us

## Flavortext
**Time for a snack ...**  

`nc binary.hashbangctf.com 7777`  

## Hint
PWNTOOLS

## Solution
This challenge was made a lot more difficult than expected because the binary wasn't given at first.  
Even when the binary was given it wasn't as straightforward as we expected. 

Auto-solution can be found in the `exploit.py` file 

Doing it manually:  
_Pick a disassembler/debugger of choice (I'm using GDB in this case)_  

- `info function` reveals that there are 3 user-defined functions  
   - order  /   main   /   **deepfatfrier**  
   
- `disas deepfatfrier` will show you that it will open a shell  
   so next step would be to try and get execution to jump to that function  

-  there's only 1 location where a payload which would succeed, that's with selection "10"  
   as the others would simply get rejected  
   
-  to overwrite the return address you need `"10" + "A"*8 + <&deepdatfrier>` 

An example payload which should technically work is   
`./whropper <<< $(python -c 'print "10"+"A"*8+"\x56\x06\x40\x00\x00\x00\x00\x00"')`

Unfortunately because the return address is 64-bit, we need to have the extra null-bytes at the end to properly overwrite the address
However this fails because the `gets()` function stops reading at the first null-byte. 

For some reason using pwntools can mitigate this issue, hence the hint suggests sending your payload through pwntools ! 

   
(For those just starting with binary I recommend watching the part in the video a well, as explaining step-by-step in text would take way too long, for experienced players just ignore this :P) 


# Flag 
FLAG{grabbin_a_byte_to_eat}

