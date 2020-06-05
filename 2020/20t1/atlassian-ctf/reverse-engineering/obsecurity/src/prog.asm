
# load some useful values
LI r12, 45
LI r13, 65
LI r14, 89
LI r15, 99
LI r8, 114

# === Write 'password: ' prompt
ADDI r1, r8, -2
OUTPUT r1
ADDI r1, r15, -2
OUTPUT r1
ADDI r1, r8, 1
OUTPUT r1
ADDI r1, r8, 1
OUTPUT r1
ADDI r1, r8, 5
OUTPUT r1
ADDI r1, r8, -3
OUTPUT r1
XOR r1, r8, r0
OUTPUT r1
LI r1, 100
OUTPUT r1
LI r1, 58
OUTPUT r1
LI r1, 32
OUTPUT r1

# === read string into memory
#addr_r4 = 0
LI r4, 0
#inchr_r5 = _input()
INPUT r5
input_loop_begin:
#if inchr_r5 == 10 goto input_loop_end
LI r1, 10
BEQ r5, r1, input_loop_end
#    memory[addr_r4] = inchr_r5
SW r4, r5
#    addr_r4 += 1
ADDI r4, r4, 1
#    inchr_r5 = _input()
INPUT r5
JMP input_loop_begin
input_loop_end:
#memory[addr_r4] = -1
ADDI r1, r0, -1
SW r4, r1

# === compare password against expected
# [48, 98, 115, 51, 99, 85, 82, 49, 116, 89, 45, 49, 115, 45, 78, 48, 45, 109, 52, 84, 67, 104, 45, 102, 48, 82]

LI r11, 1
LI r9, 0

LI r4, 0
LW r5, r4
LI r1, 48
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 98
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 115
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 51
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r15, r0
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r14, -4
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r14, -7
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 49
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r8, 2
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r14, r0
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r12, r0
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 49
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r8, 1
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r12, r0
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 78
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r12, 3
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r12, r0
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r8, -5
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 52
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r14, -5
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 67
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 104
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r12, r0
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 102
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r12, 3
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r14, -7
CMP r1, r1, r5
AND r1, r1, r11
ADD r9, r9, r1
skips:

# check length of password was correct
ADDI r4, r4, 1
LW r5, r4
ADDI r1, r0, -1
BEQ r5, r1, ok5
JMP incorrect
ok5:

# check there were no invalid chars
BEQ r9, r0, ok6
JMP incorrect
ok6:


# === correct, print flag
XOR r1, r13, r0
OUTPUT r1
ADDI r1, r14, -5
OUTPUT r1
LI r1, 76
OUTPUT r1
XOR r1, r13, r0
OUTPUT r1
ADDI r1, r14, -6
OUTPUT r1
ADDI r1, r14, -6
OUTPUT r1
LI r1, 73
OUTPUT r1
XOR r1, r13, r0
OUTPUT r1
LI r1, 78
OUTPUT r1
LI r1, 123
OUTPUT r1


LI r4, 0
LW r5, r4
XOR r1, r15, r0
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r12, r0
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 30
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r8, 4
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r14, -6
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 59
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r15, -2
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 28
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 3
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 104
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 121
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r14, r0
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 94
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r14, r0
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 126
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 95
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 0
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 32
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r13, r0
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 55
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 11
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 69
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
XOR r1, r14, r0
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r14, -2
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
LI r1, 125
XOR r1, r1, r5
OUTPUT r1

ADDI r4, r4, 1
LW r5, r4
ADDI r1, r15, -2
XOR r1, r1, r5
OUTPUT r1

LI r1, 125
OUTPUT r1
LI r1, 10
OUTPUT r1
JMP done

# === incorrect, print message
incorrect:
LI r1, 105
OUTPUT r1
ADDI r1, r8, -4
OUTPUT r1
XOR r1, r15, r0
OUTPUT r1
ADDI r1, r8, -3
OUTPUT r1
XOR r1, r8, r0
OUTPUT r1
XOR r1, r8, r0
OUTPUT r1
LI r1, 101
OUTPUT r1
XOR r1, r15, r0
OUTPUT r1
ADDI r1, r8, 2
OUTPUT r1
LI r1, 10
OUTPUT r1
done:
