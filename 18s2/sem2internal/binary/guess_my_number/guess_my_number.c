/*
   Guess My Number Version 2.0:                                                          @wingz -- 2k18
   Uses malloc and array to hide the true values from the stack, so that people can't read it muahahaha

   inspired by @ljc's rand_of_fortune
   compile with: gcc -m32 -o <out> guess_my_number.c 
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

#define SIZE 100

void flag(void) {
	FILE *f = fopen("flag.txt","r");
	char flag[SIZE] = {0};
	fread(&flag, 30, 1, f);
	fclose(f);
	printf("%s\n", flag);
}

void fail() {
	char *fail = "Sorry friend that's the wrong number !\n";
	printf(fail);
	exit(1);
}


int main(void) {
	setbuf(stdout, NULL);
	srand(time(NULL));

	int *array = malloc(sizeof(int)*2);
	array[0] = 1337;
	array[1] = rand();

	int check1 = rand();
	char *greet = "Hello stranger, do you want to know a secret?\n";
	char *intro = "But first, what is your name?\n";
	char *response = "\nHmm that's an interesting name: ";
	char *challenge = "I'll tell you my secret if you can guess my two numbers ...\n\nHere's a hint: They're at %p and %p \n\n";
	char *ask = "\nLet's see your two numbers now then: \n";
	int check2 = rand();

	int *array2 = malloc(sizeof(int)*2);
	array2[0] = 7331;
	array2[1] = rand();	

	printf(greet);
	printf(challenge, &array[1], &array2[1]);	
	printf(intro);
	fflush(stdout);

	char name[SIZE] = {0};
	fgets(&name, SIZE, stdin);

	printf(response);
	printf(name);
	printf(ask);
	fflush(stdout);

	//delet it
//	printf("[DEBUG]: %d %d\n", array[1], array2[1]);

	fflush(stdout);
	scanf("%d", &check1);
	if(check1 != array[1]) fail();

	fflush(stdout);
	scanf("%d", &check2);
	if(check2 != array2[1]) fail();
	else flag();

	free(array);
	free(array2);
	return 0;
}


