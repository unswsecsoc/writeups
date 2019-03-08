# Stegannochio

## Author
Vincent Chen

## Category
Other

## Type
Steganography

## Description
How old am I? Forever 17 of course! Haven't you read my adventurous book detailling my superb honour, tough, and grit? Wait, stop looking at my nose!

## Points
~~100~~ 150

## Hints
I'm a very significant person; just look at how many films I have. HEY! What did I JUST SAY about the nose!?

## Files
https://i.imgur.com/10a9wks.png

## Solve Script
1. `pip install -r requirements.txt`. You might want to start a venv first, or add the `--user` flag after install.
2. `python3 steg.py -h`
3. ???
4. Profit.

## Walkthrough
First things first, 
**I sincerely apologise for making such a difficult challenge for the O-Week CTF!**
This is my first time writing up a challenge for a CTF, you have no idea how relieved I was when somebody managed to solve it.

Now that's out of the way, let's get stuck into it!

### 0. Google
When you see a CTF challenge with an image in it, your mind should immediately jump to *Steganography*. 
It's the art of hiding things in plain signt, encoding messages in images or other benign file formats.

Then, have a read of some steg challenges. That was my biggest hint to people asking for tips.

### 1. RTFQ
Read The Freakin' Question. I used the age of the original book [The Adventres of Pinocchio](https://en.wikipedia.org/wiki/The_Adventures_of_Pinocchio) later.

### 2. Recon
This step was made largely unnecessary by the method I used to encode the message, but it's a worthwhile venture nonethelesss. Most steg challenges encode their bits as the *difference* between the pixel RGB values. Most.

You should reverse image search for the image. I highly recommend also image searching for relevant search terms. 
Google's reverse image search tends to work very well and you can find the image I used there.

This is the image I used. I had to scroll down a bit on the Google Image search for "Pinocchio" to find [this](https://www.ebay.com/p/RARE-Shrek-The-3rd-Pinocchio-Limited-Edition-Best-Buy-Promo-Figure-MCD-H-m/2151017963)

### 3. Cracking
This is the fun bit.

First, you should do a diff between the images. You will quickly realise that the source image is a jpeg and the challenge is a png.
This means diffing the image will result in a bunch of noise and will make it near impossible to determine which pixels were changed.
This is the point where you might throw up your hands and try another challenge. And I wouldn't blame you, it was only worth 100 points at the start.

Honestly, I wouldn't know where to start if I were solving this; ask Edgar Cheese Wheel how he did it.

The algo I used is in the script, but the gist of it is that I encoded each digit of ascii decimal into the least significant digits of each RGB value at a certain periodicity. 
Remember the age thing? That's the periodicity of the pixels.

## Flag
`OWEEK{My_NoSe_iSNT_aNY_LoNGeR_THaN_YouRS_MiSTeR_D^:}`

## Other
Next time, I'll make an easier steg for beginners, and a more difficult one with a twist ;)
