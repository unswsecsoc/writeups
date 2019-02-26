# ilikemathz

## Flavortext
can you defeat our super duper password checker thingo?!

## Hint 
print "{}{}".format(str(hash(float('infinity')))[0], chr(int(str(hash(float('infinity')))[-1:-3:-1]) -1))[::-1]

## Solution 

It's very similar to level2 of the io64 challenge. with some added operations to make things interesting  

As shown by the solver script, it is quite easy to do using the _z3_ tool. (Even the math operations hint at z3)  
Of course it is still doable by hand, but multiplying large numbers is not recommended by hand lol.

_(Please contact Jess (@raerya) for any further inquiries about this challenge)_

## Flag
FLAG{roll_them_flags_because_im_dumb_enough_to_upload_it}


## Awesome writeup by other players 
https://gist.github.com/anon1mous/69216d80a619a2e407f481bf3addf5e5

