# GTFO

## Flavortext 
Zac has left his flag in his house, can you get it for him ?   
But you have to be quick, if his roommate catches you you'll be kicked out !    

Here's his password: `pls`  

`ssh zac@gtfo.hashbangctf.com`  

## Hint
`man ssh`

## Solution
This challenge tests your knowledge of the SSH command, as the .bashrc file has been configured to autologout upon login, one easy way to bypass this is that the ssh command actually allows you to execute one command without opening a shell   
`ssh zac@gtfo.hashbangctf.com cat flag` will get you the flag.

There are other ways which players have used to solve this challenge:  
- Using `scp` to copy the file back locally for reading  
- Interrupting the login process with `^C` and therefore preventing logout  

## Answer
FLAG{#JU5T_W1NG_1T}


