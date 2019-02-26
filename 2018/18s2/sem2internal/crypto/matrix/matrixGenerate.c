#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define BYTE_BINARY_PATTERN "%c%c%c%c%c%c%c%c"
#define BYTE_TO_BINARY(byte) \
         (byte & 0x80 ? '1' : '0'), \
         (byte & 0x40 ? '1' : '0'), \
         (byte & 0x20 ? '1' : '0'), \
         (byte & 0x10 ? '1' : '0'), \
         (byte & 0x08 ? '1' : '0'), \
         (byte & 0x04 ? '1' : '0'), \
         (byte & 0x02 ? '1' : '0'), \
         (byte & 0x01 ? '1' : '0')

int main (int argc, char *argv[]) {
    char flag[] = "flag{didyouautomatethis?}";
    char cipher[50] = {0,};
    int length = strlen(flag);
    int counter = length;
    counter --;
    while (counter >= 0) {
        char letter = flag[counter]; // starts from last character
        cipher[counter] = letter;

        for (int i = counter+1; i < length; i++) {
            cipher[i] ^= letter;
        }
        counter --;

    }
    for (int i = 0; i < length; i++) {
        printf(BYTE_BINARY_PATTERN, BYTE_TO_BINARY(cipher[i]));
    }
    printf("\n");
    return 0;
}