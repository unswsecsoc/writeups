# so basic

## Flavortext 
Talking in Englsih is _soooo basicccc broooooo_   
lets use this secret language instead.  
__________________________________________
RkxBR3t3aDBfbjMzZHNfcGFkZDFuZ19hbnl3NHk/fQ


## Hint
(no hint)

## Solution
As the challenge title suggests, the flag has been encoded with [Base64](https://en.wikipedia.org/wiki/Base64)  
To get the flag just put it into an online decoder or use the command-line: 

`echo "RkxBR3t3aDBfbjMzZHNfcGFkZDFuZ19hbnl3NHk/fQ" | base64 -d`

One thing to note is that most base64 encoded strings have 1-3`=` characters at the end which act as padding, however this challenge was made not so easy by removing the padding 


## Answer
FLAG{wh0_n33ds_padd1ng_anyw4y?}


