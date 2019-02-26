# madorbad

## Flavortext
Give me the flag and i'll decrypt it.

## Hint
U mad or angry  
(Note: this is the hint for you to try and use the `angr` tool)


## Solution

**Easy way:** 
- run the provided solver script  
- learn how to use _angr_
  
**Hard way:** 
- although the source wasn't given, you could disassemble the binary to find out the function names
- a side-channel way of solving the challenge was to figure out that eg. `oOOoOOoo` corresponds to `10010011`
    - by figuring out the rest of the function names you could find out the pattern and get the flag as well

_(please contact Sean (@sy) if you have any other inquiries about this challenge)_ 

## Answer
FLAG{thank_god_i_generated_this_in_python_lol_xdlfh-(0[af}

