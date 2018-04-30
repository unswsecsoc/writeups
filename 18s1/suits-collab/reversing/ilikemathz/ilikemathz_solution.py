from pwn import *
from z3 import *

chal_name = "ilikemathz"

a = BitVec('a', 64)
b = 0x7331deadbeef1337
c = BitVec('c', 64)
d = 0x7517cafebabe7157

prob1 = (a * b)
prob2 = (c | (ord('Z') + 3))
s = Solver()
s.add(prob1 & prob2 == d)

s.check()
a_ans = str(int(s.model()[a].sexpr().replace('#','0'), 16))
c_ans = str(int(s.model()[c].sexpr().replace('#','0'), 16))

print "param[1] == {}".format(a_ans)
print "param[2] == {}".format(c_ans)

#p = process([chal_name])
p = remote("127.0.0.1", 9091)
p.sendline(a_ans)
p.recv(timeout=1)
p.sendline(c_ans)
print p.recv(timeout=1)
