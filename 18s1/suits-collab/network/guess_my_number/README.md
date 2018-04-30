# Guess My Number

## Flavortext
I'm thinking of a number from _1 to a million_ , can you guess it ?

`nc binary.hashbangctf.com 8081`

## Hint
lol no

## Solution
Using your language of choice, brute force the number with as many connections as you can make !   
If you want to be even more efficient multi-threading can help...  
Other-wise just open up _many many_ terminal sessions and start from different intervals.

example shell script:
```
for i in $(seq 1000000); do echo "$i" | nc binary.hashbangctf.com 8081; done
```
Once you hit the number `637928`, the flag will get printed

## Answer
FLAG{ouch_thats_brutal}


