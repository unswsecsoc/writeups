Title
=============
Nethackers

Description (hidden from players)
=============
Maze game with treasure that can't be reached with normal method.
Need buffer overflow to change the coordinate of the player directly to get the amulet.


Flavour (for players to see)
=============
After the Creation, the cruel god Moloch rebelled against the authority of Marduk the Creator. Moloch stole from Marduk the most powerful of all the artifacts of the gods, the Amulet of Yendor, and he hid it in the dark cavities of Gehennom, the Under World, where he now lurks, and bides his time. (source: Wikiquote)


Hints
=============
The biggest obstable here is perhaps your mind. Try casting the scroll of teleportation ;)


Running (how to run, if required)
=============
give them ONLY the binary files.


Walkthrough
=============
* this is a maze game that takes inputs: north, south, east, west from user to move the player "@"
* the goal is to get to the amulet denoted by "$"
* but upon exploring the whole maze (or not), player will find out that the $ is sealed off
* Yep, you need to change the location of @ into the exact coordinate of where $ is (x=14, y=5)
* To do that, you will need to craft an exploit with a hex editor (like hex Fiend) that puts `0E` and `05` at offset 6 and 7 followed by a `\n`.
* pipe the exploit file into the game by running the binary with redirected stdin.
* the flag will print out! :)



Flag
=============
flag{muahaha_not_the_real_amulet}

EXTRA
============

Binary compiled to give players:

`gcc nethackers.c -o <FILE>`

Binary compiled statically for the docker container

`gcc -m32 -sttaic -o nethackers nethackers.c`


Do be aware that when piping exploits that the connection will close without returning input:
so use `cat file - | nc xxxx xxxx` when using exploit files
