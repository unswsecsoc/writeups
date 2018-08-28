# Intel.js level 2

The basic idea is to figure out how the js is running and exploit the fact that 1-(-1) = 2 to bypass a value check lock.

Needs to connect to a netcat port so players can run their machine code, the code in launch works on my mac lol.

the solution is in `level_2_soln.txt`, you can test the challange by running

```
cat level_2_soln.txt | node level_2.js | tr -d '\n' | tr -d '\000' | grep -o 'flag{[^}]*}'
```

`level_2_dist.js` is the version of the code to be posted on the ctf website (with the flag hidden)

flag: `flag{m1nus_m1nus_0ne_1s_0ne?_w1ld}`


# Requirements

node to be installed.
