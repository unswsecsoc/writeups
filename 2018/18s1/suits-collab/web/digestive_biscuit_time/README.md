# ~Cookie~ Digestive Biscuit Time!
The cookie is based off time, use clues to guess admin's last login time and spoof your cookie

## Flavourtext
Are you the admin? I'm not sure you are, when are you?

## Hint
I wonder what that big number in the cookie is, man not knowing this is a epoch fail

## Running
python3 run.py

## Walkthrough
So first of all make an account and log in, then look at your cookies  
if you decode it from base64 you'll have

`<username>,<big number>`

if you delete the cookie (or logout) and log in again you'll notice  
the big number change. that's cause it's the time you last logged in as a unix time stamp

If you look at the chat board you'll see the admin brag about the sunset on the  
6th of april 2018. the sunset on the 6th of april 2018 happened at 5:44pm  

use that to work out the minute the admin logged in, then brute force the 60   
options until you get the right time.  

rewrite your cookie to be `admin,<time>`  
and see if the system recognises it or not.  
Eventually you'll hit the right Time and the system will assume you are the admin. The flag will then appear.  

your cookie has to be `YWRtaW4sMTUyMzAwMDY2Mw==` which is `admin,1523000663`  
or the unix time stamp for 6/4/2018 17:44:23 (i think lol)  

you could also get in by guessing the admin password (password12348)  

## Answer
FLAG{SUNS3TS_R_B002FU11}

