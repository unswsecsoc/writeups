Title
=============
The Force Awoken - Star Wars II


Description
=============
Login by predicting the current TFA using previous TFA.

Flavour
=============
Use your force vision


Hints
=============
RED

Running (how to run, if required)
=============
Go to ctf.justind.party/lando/login and ctf.justind.party/lando/tfa (Note the tfa might stop updating and need to be reset)


Walkthrough
=============
Step 1. Notice that the first letter of each words in the heading is highlighted in red (Aside: That’s the real reason for the Star War storyline btw :P ). A quick google of “LCG cryptography” will reveal that it is stand for “Linear Congruential Generator”. LCG is a quick and simple PRNG that is frequently used (e.g. UNIX random) but not cryptographically secure.

Step 2. There are many resources online for breaking LCG (e.g. https://security.stackexchange.com/questions/4268/cracking-a-linear-congruential-generator).
<To be expanded>

Step 3. Once the parameters (a, b, m) are retrieved by the technique above, future value of the PRNG can be found by solving the resulting systems of equations. This can be done with online tool such as https://www.dcode.fr/modular-equation-solver.

Step 4. Given that the spaceship is 45000000 km away and the message travel in light speed (300000 km/s), it will take 150 seconds to receive the message, which correspond to 5 TFA value. Therefore the correct TFA will be the 6th predicted value in the futures.

Flag
=============
flag{__such_rando_much_insecure_wow__}
