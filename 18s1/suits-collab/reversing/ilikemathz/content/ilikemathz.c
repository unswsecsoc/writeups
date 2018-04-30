#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void super_secret_password_checker(char* pass1, char* pass2){

	if(((strtoull(pass1, NULL, 10) * 0x7331deadbeef1337llu) &(strtoull(pass2, NULL, 10) | ((unsigned long long)'Z' + 3))) == 0x7517cafebabe7157){
		printf("FLAG{roll_them_flags_because_im_dumb_enough_to_upload_it}");
		fflush(stdout);
	}

}

int main(int argc, char** argv){
	int BUFF_SIZE = 21;
	
	char pass1[BUFF_SIZE];
	char pass2[BUFF_SIZE];
	printf("Input two passes separated by newlines\n");
	fflush(stdout);

	read(0, &pass1, BUFF_SIZE);
	read(0, &pass2, BUFF_SIZE);

	pass1[strcspn(pass1, "\n")] = '\0';
	pass2[strcspn(pass2, "\n")] = '\0';

	super_secret_password_checker(pass1, pass2);

	return 1337;
}
