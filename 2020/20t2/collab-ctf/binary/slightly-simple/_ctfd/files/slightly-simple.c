#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void win() {
	printf("You win! Here's a shell\n");
	system("/bin/sh");
}

void lol() {
	char buf[20];
    puts("hi");
    // we just printed out the canary for you :)
    printf("%x\n", *(int*)(buf + 20));

	gets(buf);
}

int main() {
	setbuf(stdout, NULL);
    lol();
	return 0;
}
