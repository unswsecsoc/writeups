#!/usr/bin/python3

import sys

print("Welcome to pysafe 3.0, please enter your password:")
sys.stdout.flush()
pwd = input()
if (len(pwd) == 4):
    try:
        pwd = "".join([format(ord(a), "x") for a in pwd])
    except:
        pwd = pwd[::-1]
    pwd = int(pwd, 16)
else:
    sys.exit()
try:
    stuff = str(format(pwd, 'x'))[0:4]
except:
    sys.exit()

if((pwd%5 == 4 and pwd%6 == 5)):
    pwd = abs(pwd-300100111)
else:
    sys.exit()
try:
    new_pwd = "".join([str(int(int(a)/2)) if int(int(stuff)/191+1) == len(str(pwd)) else sys.exit() for a in str(pwd)])
except:
    sys.exit()

if (int(new_pwd[4:]) == 1234):
    try:
        f=open("flag", "r")
        if f.mode == 'r':
            print(f.read())
            sys.stdout.flush()
    except:
        print("Victory!!! But flag not found, so that's weird")
        sys.stdout.flush()

