#include <stdlib.h>
#include <stdio.h>

char code[] = 

    "\xe9\x1e\x00\x00\x00"  //          jmp    8048083 <MESSAGE>
    "\xb8\x04\x00\x00\x00"  //          mov    $0x4,%eax
    "\xbb\x01\x00\x00\x00"  //          mov    $0x1,%ebx
    "\x59"                  //          pop    %ecx
    "\xba\x0f\x00\x00\x00"  //          mov    $0xf,%edx
    "\xcd\x80"              //          int    $0x80
    "\xb8\x01\x00\x00\x00"  //          mov    $0x1,%eax
    "\xbb\x00\x00\x00\x00"  //          mov    $0x0,%ebx
    "\xcd\x80"              //          int    $0x80
    "\xe8\xdd\xff\xff\xff"  //          call   8048065 <GOBACK>
    "\x66\x6c\x61\x67\x7b"  // OR       "\x48\x65\x6c\x6c\x6f\x2c\x20\x57"
    "\x64\x33\x63\x72\x79"  //          "\x6f\x72\x6c\x64\x21\x0d\x0a"
    "\x70\x54\x7d\r\n";	    // '\x66\x6c\x61\x67\x7b\x64\x33\x63\x72\x79\x70\x54\x7d'

int main(int argc, char **argv)
{
    (*(void(*)())code)();

    return 0;
}
