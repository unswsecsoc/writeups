from pwn import *
from math import gcd
from primes import primes

def lcm(a ,b):
    return a * b // gcd(a, b)

proc = process(["python3", "./app.py"])

# stage 1: calculate q from n and p
# which is q = n / p
print(proc.recvuntil("Navigation = ").decode())
n = int(proc.recvuntil(" ", drop = True))
log.info("n = {}".format(n))
print(proc.recvuntil("Power = ").decode())
p = int(proc.recvuntil(" ", drop = True))
log.info("p = {}".format(p))
q = int(n / p)
log.success("q = {}".format(q))
proc.sendline(str(q))

# stage 2: calculate d given n and e
# where (d % lambda(n)) == (e^-1 % lambda(n))
# or d*e % lambda(n) == 1
# we find lambda(n) = lcm(p - 1, q - 1)
# first find p and q
print(proc.recvuntil("N = ").decode())
n = int(proc.recvuntil(",", drop = True))
log.info("n = {}".format(n))
print(proc.recvuntil("E = ").decode())
e = int(proc.recvuntil("!", drop = True))
log.info("e = {}".format(e))
# loop through and find all prime factors of n
# but notice that n is even so 1 of the factors is 2
p = 2
log.success("p = {}".format(p))
q = int(n / p)
log.success("q = {}".format(q))
# then we find lambda by using lcm(p - 1, q - 1)
ld = lcm(p - 1, q - 1)
# finally find any d that gives us d*e % lambda(n) == 1
d = 1
while True:
    if (d * e) % ld == 1: break
    d += 1
log.success("d = {}".format(d))
proc.sendline(str(d))

# stage 3
# follow online resource on RSA to get private key d
print(proc.recvuntil("crypt = ").decode())
c = int(proc.recvuntil(" ", drop = True))
log.info("c = {}".format(c))
print(proc.recvuntil("P = ").decode())
p = int(proc.recvuntil(",", drop = True))
log.info("p = {}".format(p))
print(proc.recvuntil("Q = ").decode())
q = int(proc.recvuntil(" ", drop = True))
log.info("q = {}".format(q))
print(proc.recvuntil("E = ").decode())
e = int(proc.recvuntil("?", drop = True))
log.info("e = {}".format(e))
n = p * q
log.success("n = {}".format(n))
ld = lcm(p - 1, q - 1)
k = 1
while True:
    if (k * ld + 1) % e == 0:
        d = int((k * ld + 1) / e)
        break
    k += 1
log.success("d = {}".format(d))
m = pow(c, d, n) #(c ** d) % n
log.success("m = {}".format(m))
proc.sendline(str(m))

# stage 4
# figure out that common exponent e is 65537
# or try to answer wrong number and check the hints
e = 65537
# then repeat stage 3 (but need to find p and q first)
print(proc.recvuntil("co_e ").decode())
c = int(proc.recvline())
log.info("c = {}".format(c))
print(proc.recvuntil("_av_gat_on = ").decode())
n = int(proc.recvuntil(" ", drop = True))
log.info("n = {}".format(n))
for i in primes:
    if n % i == 0:
        p = i
        q = int(n / p)
        break
log.success("p = {}".format(p))
log.success("q = {}".format(q))
ld = lcm(p - 1, q - 1)
k = 1
while True:
    if (k * ld + 1) % e == 0:
        d = int((k * ld + 1) / e)
        break
    k += 1
log.success("d = {}".format(d))
m = pow(c, d, n) #(c ** d) % n
log.success("m = {}".format(m))
proc.sendline(str(m))

proc.interactive()