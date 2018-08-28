# Intel.js level 1

The basic idea is to figure out how the js is running a made up assembly language so you can write your own code to read from the part of memory where the flag is.

Needs to connect to a netcat port so players can run their machine code, the code in launch works on my mac lol.

the solution is in `level_1_soln.txt`, you can test the challange by running

```
cat level_1_soln.txt | node level_1.js | tr -d '\n' | tr -d '\000' | grep -o 'flag{[^}]*}'
```

`level_1_dist.js` is the version of the code to be posted on the ctf website (with the flag hidden)

flag: flag{0ne_r3g1st3r_1s_m0r3_th3n_3n0ugh}


# Requirements

node to be installed.
