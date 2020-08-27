#include <stdio.h>
#include <stdlib.h>

void vuln() {
	char buf[30];
	puts("Crash me to 1337%256");
	gets(buf);
}

int main() {
	setbuf(stdout, NULL);
	vuln();
	exit(1);
}