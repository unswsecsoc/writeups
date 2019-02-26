# Intel.js level 3

Same as before but the code is restructured to actually copy instructions into memory and use a program counter / memory based execution.

The entire thing is laps minified and all variable names replaced with 'o's

the solution is in `level_3_soln.txt`, you can test the challange by running

```
cat level_3_soln.txt | node level_3.js | tr -d '\n' | tr -d '\000' | grep -o 'flag{[^}]*}'
```

`level_3_dist.js` is the version of the code to be posted on the ctf website (with the flag hidden)

flag: `flag{ooOOOooOOOooOOOOoo}`


# Requirements

node to be installed.
