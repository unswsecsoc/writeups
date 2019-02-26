# Gimme! Gimme! Gimme!

## Author
* evan

## Category
reversing

## Type
* query
* bot
* ask
* time
* lyrics

## Description
### Gimme! Gimme! Gimme! (A Flag After Midnight)
#### [Help Agnetha get that flag and chase the shadows away 🎶](http://cgi.cse.unsw.edu.au/~evank/other/gimme/gimme.cgi/)

## Points
50

## Hints
1. Experiment a lot, but be very systematic.

## Files
* gimme.cgi: intial file to run
* run.py: main challenge logic file
* lyrics.txt: file of the song lyrics
* templates: contains html template

## Walkthrough
1. Experiment with different options
2. Find that multiple uses of the phrase "gimme" gives various forms of output
3. Systematically work through the outputs of "gimmie" * n for 1 <= n <= 30 (which is the number of "gimme"s in the song)
4. Either notice strange output in the daytime, asking you to rethink about what Agnetha says, or earn the flag if the time is between midnight and dawn (gimmie a man after midnight ... till the break of the day)

## Flag
`FLAG{&_!_g4z3_1nt0_th3_n!ght}`

