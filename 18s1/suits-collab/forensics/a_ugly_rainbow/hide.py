#!/usr/bin/env python3
import sys
import os
import random
import math

# msg is a string
msg = "FLAG{i_3ncrypt_w1th_h3x_vry_s3cvre}"[::-1]
# width is in num circles per line
w = 20
# radius of each circle
r = 20
# size is in characters (size/12 must be a square number)
size = 768

# svg magic
w+=1
if len(msg)%2 != 0:
	msg += "."

total = size-len(msg)
raw = []

for i in range(total):
	raw.append(random.SystemRandom().randint(33, 126))

i = random.SystemRandom().randint(0, len(raw)-len(msg))
raw = raw[:i]+[ord(x) for x in msg]+raw[i+1:]

raw = [hex(x)[2:].upper() for x in raw]

while len(raw) % 3 != 0:
	raw.append("00")

colors = []
i = 0
curr = "#"
for e in raw:
	if i == 3:
		colors.append(curr)
		curr = "#"
		i = 0
	curr += e
	i+=1

final = []
x = 0
y = 1
for col in colors:
	x += 1
	if x > w:
		x = 1
		y += 1
	final.append("<circle cx='%d' cy='%d' r='%d' fill='%s'/>"%(x*2*r,y*2*r,r,col))

final = ["<svg height='%d' width='%d' xmlns='http://www.w3.org/2000/svg'>"%((w+1)*2*r,(w+1)*2*r)] + final + ["</svg>"]
f = open("secret.svg","w")
for l in final:
	f.write(l)
	f.write("\n")
f.close()
