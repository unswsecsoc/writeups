#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int readByte(char *output) {
    char c1,c2,c3,c4,c5,c6,c7,c8;
    int ret = scanf("%c%c%c%c%c%c%c%c", &c1,&c2,&c3,&c4,&c5,&c6,&c7,&c8);
    *output = (c1 == '1' ? 0x80 : 0) 
            | (c2 == '1' ? 0x40 : 0)
            | (c3 == '1' ? 0x20 : 0)
            | (c4 == '1' ? 0x10 : 0)
            | (c5 == '1' ? 0x08 : 0)
            | (c6 == '1' ? 0x04 : 0)
            | (c7 == '1' ? 0x02 : 0)
            | (c8 == '1' ? 0x01 : 0);
    return ret;
}

int main (int argc, char *argv[]) {
    char input[255];
    int length = 0;
    while (readByte(&input[length]) != EOF) {
        length++;
    } 
    input[length] = 0;
    for (int counter = 0; counter < length; counter++) {
        for (int i = counter + 1; i < length; i ++) {
            input[i] ^= input[counter];
        }
    }
    printf("%s\n", input); 
    return 0;
}