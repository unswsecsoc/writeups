# s c r o n c h

## Flavortext

orang: i cant descronch
 
meme man: you needst to u n s c r o m b l e 

orang: wtf 


}LRMISETLVC$NAWUGFBOODARHYOCEMSJD{MGE
(omit the dollar sign from your submission)

## Description

Decoding a burrows-wheeler transform (does the hint make this too obvious?)
This challenge can be made more difficult by omitting the terminating marker (leaving them to brute-force the position of the marker)

## Hint

though this be madness, yet there is method in 'bwt

## How2pwn

### EZ mode

1. Decode with http://guanine.evolbio.mpg.de/cgi-bin/bwt/bwt.cgi.pl

### Manual

1. Let S be the encoded string. Disambiguate duplicate characters by appending a unique digit to it.
2. Sort S in order of increasing ASCII values to obtain S'. Duplicate characters will be sorted by the disambiguating digit (increasing order)
3. Let F be a list for holding the characters of the final flag. It is currently empty.
4. Prepend S'[0] (should be '$') to F. Let x be the character S[0]. 
5. Prepend x to F, and find x in S'
6. Let i be the index of x in S. Set x to be S'[i]
7. Repeat steps 5 and 6 until F and S are equal in length. F should now contain the flag.
8. Example (because this is hard to put into words): youtu.be/DqdjbK68l3s?t=9m30s

## Flag

FLAG{WHOMSTDVESCROMBLEDMYORANGJUICE}
