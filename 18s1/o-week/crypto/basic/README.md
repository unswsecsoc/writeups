# Basic

## Author
* zac

## Category
cyrpto

## Type
* base64
* encoding

## Description
This challenge brings me back to simpler more *basic* times, like when I was young and used to play on my n*64*. But one day it broke, and all I could get out of it was this weird error message.

```
BEGIN ERROR
---------------------------------------------------
T29oISBJdCB3b3JrZWQhIFlheQ==
SG1tLCBraW5kYSBjbG9zZQ==
QXJlIHlvdSByZWFsbHkgZ29pbmcgdG8=
TG9va3MgbGlrZSBpdA==
VGhhdCdzIGtpbmRhIHNpbGx5Li4uLg==
VGhlcmUncyBhIG5lYXRlciB3YXk=
cGxzIHN0YXA=
WW91IGRvIG5vdCBrbm8gZGEgd2FlIQ==
RkxBR3tUcnktVHJ5LUFnYWlufQ==
U29ycnkhIE5vdCBoZXJlIQ==
aWYgYXQgZmlyc3QgeW91IGRvbid0IHN1Y2NlZWQ=
---------------------------------------------
END ERROR
```

## Points
30

## Hints
1. I wonder why these messages end with equal signs...

## Walkthrough
1. For every line in the message
2. Use base64 decode it
3. Find the flag in one of the messages

## Flag
`FLAG{Try-Try-Again}`

