#include <stdio.h>
#include <stdlib.h>


void deepfatfrier(void){
	system("/bin/sh");
}

void order(char *selection){

		printf("Welcome to McWhropper!\n\nWhat would you like to order today?\n\n");
		printf("1: Double McWhropper with extra spicy pawn sauce\n");
		printf("2: Mini Ropper with fries\n");
		printf("3: Deep Fried Canary\n");
		printf("4: Stack Rack of Ribs\n");
		printf("5: SHELL shake\n");
		printf("6: Apple PIE\n");
		printf("7: NOP sliders\n");
		printf("8: Pancake with hackery sauce\n");
		printf("9: Bits of bacon\n");
		printf("10: Buffer buffet\n");
		fflush(stdout);

		int flag = 1;
		while(flag){
			gets(selection);
			switch (atoi(selection)) {
				case 1:
				case 2:
				case 3:
				case 4:
				case 5:
				case 6:
				case 7:
				case 8:
				case 9: printf("Unfortunately we have run out at this time.\nPlease select another order\n");
					fflush(stdout);
					break;
				case 10: printf("Excellent selection!\n"); flag = 0;
					fflush(stdout);
					break;
				default: printf("Invalid Order\n");
					fflush(stdout);
			}
		}
}

int main(void){
	char selection[2];
	order(selection);
	return 0;
}
