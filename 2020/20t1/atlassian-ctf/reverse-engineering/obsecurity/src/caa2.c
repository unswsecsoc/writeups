#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

// util functions
static int signex(int value);
static int intcmp(int a, int b);

// opcodes
enum opcode {
    OP_NOP, OP_SHL, OP_INVALID_1, OP_INVALID_2,
    OP_XOR, OP_AND, OP_ADD, OP_ADDI,
    OP_LW, OP_SW, OP_CMP, OP_INPUT,
    OP_BEQ, OP_BNE, OP_J, OP_OUTPUT
};

// vm entry point
int main(void) {
    // open file
    FILE* f = fopen("prog.bin", "rb");
    if (f == NULL) {
        fprintf(stderr, "error: unable to open prog.bin\n");
        return 1;
    }

    // set up memory
    uint16_t* imem = malloc(512 * sizeof(uint16_t));
    uint32_t* dmem = malloc(512 * sizeof(uint32_t));

    // load program from file
    if (fread(imem, sizeof(uint16_t), 512, f) != 512) {
        fprintf(stderr, "error: prog.bin must be 512 bytes\n");
        return 1;
    }

    // initialize vm state
    uint32_t registers[16] = {};
    int pc = 0;

    // execute each instruction
    while (pc < 512) {
        // instruction fetch/decode
        int instr = imem[pc];
        enum opcode opcode = (instr >> 12) & 0x0f;
        int rd = (instr >> 8) & 0x0f;
        int rs = (instr >> 4) & 0x0f;
        int rt = instr & 0x0f;
        int imm = signex(rt);
        int wide_imm = instr & 0xfff;

        // execute
        int next_pc = pc + 1;
        switch (opcode) {
            // NOP : do nothing
            case OP_NOP:
            break;

            // SHL : shift rs left by imm, store in rd
            case OP_SHL:
            if (imm > 0) {
                registers[rd] = registers[rs] << imm;
            } else {
                registers[rd] = registers[rs] >> imm;
            }
            break;

            // XOR : xor rs with rt, store in rd
            case OP_XOR:
            registers[rd] = registers[rs] ^ registers[rt];
            break;

            // AND : and rs with rt, store in rd
            case OP_AND:
            registers[rd] = registers[rs] & registers[rt];
            break;

            // ADD : add rs to rt, store in rd
            case OP_ADD:
            registers[rd] = registers[rs] + registers[rt];
            break;

            // ADDI : add rs to imm, store in rd
            case OP_ADDI:
            registers[rd] = registers[rs] + imm;
            break;

            // LW : load word from memory addres rs into rd
            case OP_LW:
            registers[rd] = dmem[registers[rs] & (512-1)];
            break;

            // SW : store rt into word at memory address rs
            case OP_SW:
            dmem[registers[rs] & (512-1)] = registers[rt];
            break;

            // CMP : compare rs to rt, store the result in rd
            case OP_CMP:
            registers[rd] = intcmp(registers[rs], registers[rt]);
            break;

            // INPUT : read character from user, store in rd
            case OP_INPUT:
            registers[rd] = getc(stdin);
            break;

            // BEQ : branch if rs and rd are equal
            case OP_BEQ:
            if (registers[rs] == registers[rd]) {
                next_pc = pc + imm;
            }
            break;

            // BNE : branch if rs and rd are not equal
            case OP_BNE:
            if (registers[rs] != registers[rd]) {
                next_pc = pc + imm;
            }
            break;

            // J : jump to address
            case OP_J:
            next_pc = wide_imm;
            break;

            // OUTPUT : write character from rs to output
            case OP_OUTPUT:
            putc(registers[rs], stdout);
            break;

            // handle invalid opcodes
            default:
            printf("invalid opcode %d\n", opcode);
        }

        // update state
        pc = next_pc;
        registers[0] = 0;
    }

    return 0;
}

// sign extend 4 bit value to 32 bits
static int signex(int value) {
    if (value & 0x8) {
        return value | 0xfffffff8;
    } else {
        return value + 1;
    }
}

// return the sign of a-b
static int intcmp(int a, int b) {
    if (a < b) {
        return -1;
    } else if (a > b) {
        return 1;
    } else {
        return 0;
    }
}
