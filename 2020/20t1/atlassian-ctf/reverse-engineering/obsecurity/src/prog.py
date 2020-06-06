# pseudocode version of the password program in python

# helpers
import sys
def _input():
    return ord(sys.stdin.read(1))
def _output(code):
    sys.stdout.write(chr(code))
    sys.stdout.flush()
memory = [0]*256
def error():
    _output(105)
    _output(110)
    _output(99)
    _output(111)
    _output(114)
    _output(114)
    _output(101)
    _output(99)
    _output(116)
    _output(10)
    assert False
    sys.exit(-1)

# begin

# === Write 'password: ' prompt
_output(112)
_output(97)
_output(115)
_output(115)
_output(119)
_output(111)
_output(114)
_output(100)
_output(58)
_output(32)

# === read string into memory
addr_r4 = 0
inchr_r5 = _input()
while inchr_r5 != 10:
    memory[addr_r4] = inchr_r5
    addr_r4 += 1
    inchr_r5 = _input()
memory[addr_r4] = -1

# === compare password against expected
# [48, 98, 115, 51, 99, 85, 82, 49, 116, 89, 45, 49, 115, 45, 78, 48, 45, 109, 52, 84, 67, 104, 45, 102, 48, 82]

addr_r4 = 0
r1 = 3
r2 = r1 << 4
assert r2 == 48
if memory[addr_r4] != r2:
    error()
addr_r4 += 1
r3 = r2 << 1
r3 = r3 + 2
assert r3 == 98
if memory[addr_r4] != r3:
    error()
addr_r4 += 1
r6 = r3 + 8
r6 = r6 + 8
assert r6 == 114
if memory[addr_r4] != r6+1: # 115
    error()
addr_r4 += 1
if memory[addr_r4] != r2+3: # 51
    error()
addr_r4 += 1
if memory[addr_r4] != r3+1: # 99
    error()
addr_r4 += 1
r7 = r2-8
r7 = r7 << 1
assert r7 == 80
if memory[addr_r4] != r7+5: # 85
    error()
addr_r4 += 1
if memory[addr_r4] != r7+2: # 82
    error()
addr_r4 += 1
if memory[addr_r4] != r2+1: # 49
    error()
addr_r4 += 1
if memory[addr_r4] != r6+2: # 116
    error()
addr_r4 += 1
r8 = r2 - 3
assert r8 == 45
if memory[addr_r4] != (r8<<1)-1: # 89
    error()
addr_r4 += 1
if memory[addr_r4] != r8:
    error()
addr_r4 += 1
if memory[addr_r4] != r2+1: # 49
    error()
addr_r4 += 1
if memory[addr_r4] != r6+1: #115
    error()
addr_r4 += 1
if memory[addr_r4] != r8:
    error()
addr_r4 += 1
if memory[addr_r4] != r7-2: #78
    error()
addr_r4 += 1
if memory[addr_r4] != r8 + 3: #48
    error()
addr_r4 += 1
if memory[addr_r4] != r8: # 45
    error()
addr_r4 += 1
r2 = r2 + 4
assert r2 == 52
if memory[addr_r4] != (r2<<1)+5: # 109
    error()
addr_r4 += 1
if memory[addr_r4] != r2: #52
    error()
addr_r4 += 1
if memory[addr_r4] != r7+4: # 84
    error()
addr_r4 += 1
if memory[addr_r4] != (1<<6)+3: # 67
    error()
addr_r4 += 1
if memory[addr_r4] != r3+6: # 104
    error()
addr_r4 += 1
if memory[addr_r4] != r8:
    error()
addr_r4 += 1
if memory[addr_r4] != r3+4: # 102
    error()
addr_r4 += 1
if memory[addr_r4] != r8+3: #48
    error()
addr_r4 += 1
if memory[addr_r4] != r7+2: #82
    error()


# === password correct, print flag
_output(65)
_output(84)
_output(76)
_output(65)
_output(83)
_output(83)
_output(73)
_output(65)
_output(78)
_output(123)
# raw flag: [83, 79, 109, 69, 48, 110, 51, 45, 119, 49, 84, 104, 45, 116, 48, 111, 45, 77, 117, 99, 72, 45, 116, 49, 77, 51]
# xor: [99, 45, 30, 118, 83, 59, 97, 28, 3, 104, 121, 89, 94, 89, 126, 95, 0, 32, 65, 55, 11, 69, 89, 87, 125, 97]

addr_r4 = 0
_output(memory[addr_r4] ^ 99)
addr_r4 += 1
_output(memory[addr_r4] ^ 45)
addr_r4 += 1
_output(memory[addr_r4] ^ 30)
addr_r4 += 1
_output(memory[addr_r4] ^ 118)
addr_r4 += 1
_output(memory[addr_r4] ^ 83)
addr_r4 += 1
_output(memory[addr_r4] ^ 59)
addr_r4 += 1
_output(memory[addr_r4] ^ 97)
addr_r4 += 1
_output(memory[addr_r4] ^ 28)
addr_r4 += 1
_output(memory[addr_r4] ^ 3)
addr_r4 += 1
_output(memory[addr_r4] ^ 104)
addr_r4 += 1
_output(memory[addr_r4] ^ 121)
addr_r4 += 1
_output(memory[addr_r4] ^ 89)
addr_r4 += 1
_output(memory[addr_r4] ^ 94)
addr_r4 += 1
_output(memory[addr_r4] ^ 89)
addr_r4 += 1
_output(memory[addr_r4] ^ 126)
addr_r4 += 1
_output(memory[addr_r4] ^ 95)
addr_r4 += 1
_output(memory[addr_r4] ^ 0)
addr_r4 += 1
_output(memory[addr_r4] ^ 32)
addr_r4 += 1
_output(memory[addr_r4] ^ 65)
addr_r4 += 1
_output(memory[addr_r4] ^ 55)
addr_r4 += 1
_output(memory[addr_r4] ^ 11)
addr_r4 += 1
_output(memory[addr_r4] ^ 69)
addr_r4 += 1
_output(memory[addr_r4] ^ 89)
addr_r4 += 1
_output(memory[addr_r4] ^ 87)
addr_r4 += 1
_output(memory[addr_r4] ^ 125)
addr_r4 += 1
_output(memory[addr_r4] ^ 97)
_output(125)
_output(10)

# PASS: 0bs3cUR1tY-1s-N0-m4TCh-f0R
# FLAG: SOmE0n3-w1Th-t0o-MucH-t1M3
