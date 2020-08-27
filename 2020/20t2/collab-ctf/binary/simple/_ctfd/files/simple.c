#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void win() {
	printf("You win! Here's a shell\n");
	system("/bin/sh");
}

int main() {
	setbuf(stdout, NULL);

	int lol = 0;
	char buf[20];
	gets(buf);
	if (lol == 0x37333331) {
		win();
	} else {
		printf("You lose.\n");
	}
}
