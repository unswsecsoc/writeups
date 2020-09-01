from pwn import *
import re

RE_QUESTION = re.compile(r'What\'s (.*?)( in (octal|decimal|hexadecimal|binary))?\?')

def get_question(q):
    q = q.decode('ascii', 'ignore').split("\n")[-1]
    print(q)
    ans = RE_QUESTION.match(q)
    if ans.group(2):
        return (ans.group(1), ans.group(3))
    return (ans.group(1), 'decimal')

p = remote('localhost', 1337)

for i in range(10):
    q = get_question(p.recvuntil("? "))
    num = eval(q[0])
    if q[1] == 'hexadecimal':
        p.sendline(hex(num)) 
    elif q[1] == 'octal':
        p.sendline(oct(num)) 
    elif q[1] == 'binary':
        p.sendline(bin(num)) 
    elif q[1] == 'decimal':
        p.sendline(str(num)) 
    print(num)

print(p.recvline().decode('ascii', 'ignore').strip())
print(p.recvline().decode('ascii', 'ignore').strip())
print(p.recvline().decode('ascii', 'ignore').strip())
print(p.recvline().decode('ascii', 'ignore').strip())
