#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


with open("./flag") as f:
    payload = f.read().strip()

def header():
    return '''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
'''

def get_func_name(val):
    assert(len(val) == 1)
    func_name = "{0:08b}".format(ord(val)).replace("0", "o").replace("1", "O")
    return func_name

def generate_func(val):
    assert(len(val) == 1)
    func_name = get_func_name(val)

    random_xor = random.randint(0, 255)
    expected_xor = ord(val) ^ random_xor
    return '''
int '''+ func_name + ''' (char c) {
    return (c ^ ''' + str(random_xor) + ''') == ''' + str(expected_xor) + ''';
}'''

def generate_check_rand(val, idx):
    assert(len(val) == 1)
    func_name = get_func_name(val)
    randxor1 = random.randint(0, 255)
    randxor2 = idx ^ randxor1
    return '''
    if (!''' + func_name + '''(word['''+ str(randxor2) + ''' ^ '''+ str(randxor1) + ''']))
        goto fail;'''

def generate_check(val, idx):
    assert(len(val) == 1)
    func_name = get_func_name(val)
    randxor1 = random.randint(0, 255)
    randxor2 = ord(val) ^ randxor1
    return '''
    if (!''' + func_name + '''(word['''+ str(idx) + ''']))
        goto fail;'''

def generate_main():
    return '''
int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: ./madorbad <string>");
        fflush(stdout);
    }

    char* word = argv[1];
    printf("You're input is %s\\n", word);
    if (strlen(word) != ''' + str(len(payload)) + ''') {
        printf("Incorrect Length\\n");
        fflush(stdout);
    }
'''

def generate_main_end():
    return '''
    printf(":>\\n");
    return 0;

fail:
    printf(":<\\n");
    exit(-1);
}
'''

def generate_main_checks(payload):
    chunk = []
    for idx, c in enumerate(payload):
        chunk.append(generate_check_rand(c, idx))

    #  random.shuffle(chunk)
    ret = ''
    for c in chunk:
        ret += c
    return ret


def main():
    output = ''
    output += header()
    seen = set()
    for c in payload:
        if c in seen:
            continue

        seen.add(c)
        output += generate_func(c)

    output += generate_main()
    output += generate_main_checks(payload)
    output += generate_main_end()
    print(output)


if __name__ == "__main__":
    main()
