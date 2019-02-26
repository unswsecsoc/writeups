# Happy Chinese New Year!

## Author
* colin

## Category
Cryptography

## Type
* permutation
* cipher

## Description
#### This challenge was previously broken, sorry about that!
You've been visited by money cat!

```
   /\       /\
  / ".-'"'-." \
 ;   _     _   ;
 ;  (0)   (0) _;_
  \   = Y =  (,,,)
   .   ._.   | -,
  .(________/   ;
 . __ (MN)   .  ;
/     )        ,
;  --'          ;
 - __  - , __  .
  (,,,)   (,,,)
```
You will prosper with bountiful, shiny internet points, but only if you can decipher the flag:

`FOHTYGEALFGDO}{EAGOR`

## Points
40

## Hints
* Maybe if you did this challenge on paper, you'll find a good place to start...

## Files
* encode.py: Encodes a given flag with a given step size 

## Walkthrough
1. Start at the first character
2. Delete it and add it to a new string
3. Go forward by 8 steps, continouing from the start if stepping off the end
4. Repeat steps 2-4 until all characters are crossed out.

## Flag
`FLAG{YEAROFTHEDOGGO}`

