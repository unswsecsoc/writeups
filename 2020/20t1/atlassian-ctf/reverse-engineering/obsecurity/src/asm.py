
# LISTING = """
# NEXT r1
# NOP 0
# NEXT r2
# ADD r5, r1, r2
# NEXT r3
# NEXT r4
# me_nop:
# NOP 0
# JMP me_nop
# """

LISTING = open("prog.asm").read()

VERILOG_MODE = False

OPCODES = [
    "NOP", "SHL", "X2", "X3",
    "XOR", "AND", "ADD", "ADDI",
    'LW', 'SW', 'CMP', 'INPUT',
    'BEQ', 'BNE', 'JMP', 'OUTPUT', 'LI'
]

OP_000 = 0
OP_DSI = 1
OP_DST = 2
OP_DS0 = 3
OP_0ST = 4
OP_D00 = 5
OP_BRANCH = 6
OP_JUMP = 7
OP_0S0 = 8
OP_SPECIAL_LI = 9

OPTYPES = [
    OP_000, OP_DSI, None, None,
    OP_DST, OP_DST, OP_DST, OP_DSI,
    OP_DS0, OP_0ST, OP_DST, OP_D00,
    OP_BRANCH, OP_BRANCH, OP_JUMP, OP_0S0, OP_SPECIAL_LI
]

import struct

lines = []
labels = {}
out = []
for line in LISTING.split('\n'):
    if '#' in line:
        line = line.split('#')[0]
    line = line.strip()
    if len(line) > 0:
        lines.append(line)

def reg(name):
    return int(name[1:])

def assemble(is_first_pass):
    for line in lines:
        if ':' in line:
            if is_first_pass:
                labels[line[:-1]] = len(out)
        else:
            opcode, args = line.split(' ', 1)
            args = args.split(', ')

            op_id = OPCODES.index(opcode)
            op_type = OPTYPES[op_id]

            if op_type == OP_000:
                out.append(op_id << 12)
            elif op_type == OP_DSI:
                imm = int(args[2])
                assert imm != 0
                if imm < -8 or imm > 8:
                    print("IMMEDIATE TOO LARGE")
                    print(line)
                    assert False
                if imm > 0:
                    imm -= 1
                else:
                    imm += 16
                out.append(
                    op_id << 12 |
                    reg(args[0]) << 8 |
                    reg(args[1]) << 4 |
                    imm
                )
            elif op_type == OP_DST:
                out.append(
                    op_id << 12 |
                    reg(args[0]) << 8 |
                    reg(args[1]) << 4 |
                    reg(args[2])
                )
            elif op_type == OP_DS0:
                out.append(
                    op_id << 12 |
                    reg(args[0]) << 8 |
                    reg(args[1]) << 4
                )
            elif op_type == OP_0ST:
                out.append(
                    op_id << 12 |
                    reg(args[0]) << 4 |
                    reg(args[1])
                )
            elif op_type == OP_D00:
                out.append(
                    op_id << 12 |
                    reg(args[0]) << 8
                )
            elif op_type == OP_0S0:
                out.append(
                    op_id << 12 |
                    reg(args[0]) << 4
                )
            elif op_type == OP_BRANCH:
                addr = len(out)
                dest = addr + 1
                if not is_first_pass:
                    if args[2] not in labels:
                        print("LABEL NOT FOUND")
                        print(line)
                        assert False
                    dest = labels[args[2]]
                delta = dest - addr
                if delta == 0:
                    print("CANNOT BRANCH TO SELF")
                    print(line)
                    assert False
                if delta < -8 or delta > 8:
                    print("BRANCH TOO FAR")
                    print(line)
                    assert False
                if delta > 0:
                    delta -= 1
                else:
                    delta += 16
                out.append(
                    op_id << 12 |
                    reg(args[0]) << 8 |
                    reg(args[1]) << 4 |
                    delta
                )
            elif op_type == OP_JUMP:
                dest = 0
                if not is_first_pass:
                    if args[0] not in labels:
                        print("LABEL NOT FOUND")
                        print(line)
                        assert False
                    dest = labels[args[0]]
                out.append(
                    op_id << 12 |
                    dest
                )
            elif op_type == OP_SPECIAL_LI:
                imm = int(args[1])
                parts = []
                while imm > 0:
                    parts.append(imm & 0x07)
                    imm = imm >> 3
                if len(parts) > 0:
                    out.append(
                        7 << 12 | # ADDI
                        reg(args[0]) << 8 |
                        0 << 4 |
                        parts[-1]-1
                    )
                else:
                    out.append(
                        4 << 12 |
                        reg(args[0]) << 8
                    )
                for seg in list(reversed(parts))[1:]:
                    out.append(
                        1 << 12 | # SHL
                        reg(args[0]) << 8 |
                        reg(args[0]) << 4 |
                        2
                    )
                    if seg != 0:
                        out.append(
                            7 << 12 | # ADDI
                            reg(args[0]) << 8 |
                            reg(args[0]) << 4 |
                            seg-1
                        )

assemble(True)
out = []
assemble(False)

print(str(len(out)) + " / 512 instrs")
assert len(out) <= 512

with open('prog.bin', 'wb') as f:
    for instr in out:
        f.write(struct.pack("<H", instr))
    for i in range(512 - len(out)):
        f.write(b'\x00\x00')
