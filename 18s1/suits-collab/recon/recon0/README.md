# Recon 0

## Flavortext
`ssh ctf@recon0.hashbangctf.com` ... and start searching !  
password: `recon0`  


## Hint
It's not in a file somewhere if that's what you were wondering


## Solution
After SSH-ing into the server, depending on whether you've seen the hint or exhausted all other posibilities
you can do two things to get the flag
1.  Use `env` to reveal the parts
2.  `cat .bashrc` to reveal the parts

```
part14=P
part15=T
part16=O
part17=}
part10=K
part11=U
part12=R
part13=I
part5=J
part4={
part7=V
part6=A
part1=L
part0=F
part3=G
part2=A
part9=S
part8=A
```
Once all the parts have been revealed just reassemble them to get the flag 


## Flag
FLAG{JAVASKURIPTO}


