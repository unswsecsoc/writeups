# Animal Memes

## Author
* vivian

## Category
Web

## Type
* XSS

## Description
Well all know the purpose of the internet is to share memes with one another. Can you help us test a site we made for that purpose?

[Click here!](http://35.189.29.60/)

*Come see us once you're done to demonstrate your success*

Alternatively, ping @viv on slack if you want confirmation and can't come in person.

## Points
50

## Hints
1. [Concepts of XSS](https://www.youtube.com/watch?v=L5l9lSnNMxg)
2. [XSS Cheat Sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet)

## Files
* xss.html: html page for challenge
* xss.css: css styling for the html

## WALKTHROUGH:
1. Find a working url to an image for the second field.
2. Put in any valid name for the first field.
3. insert the injection script: `https://path_to_your_image.com/meme/' onload='alert("Yay! I just won the best meme!");`
4. Take note of the single/double quotes as it is important to get them right

# Other
This is a fairly simple cross-sites scripting CTF challenge.
Everything is done on a single webpage on the client side.
