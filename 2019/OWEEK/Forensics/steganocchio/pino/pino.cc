// extract values from pinocchio image by Eidar Cheese Wedge (Matthew Turner)
// usage: `pino <file1>` to extract least significant decimal digit (prints in BGR order)
// usage: `pino <file1> <file2>` to compare RGB values between two images
// note: best to convert source png to jpg first; stb_image has a poor jpeg loader
// public domain or whatever

#define STB_IMAGE_IMPLEMENTATION
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image.h"
#include "stb_image_write.h"

#include <stdio.h>

int main(int argc, char** argv) {
	int x,y,n;
	if (argc < 2) {printf("usage: pino <fname>\n"); return -1;}
	unsigned char *data = stbi_load(argv[1], &x, &y, &n, 3);
	if (!data) {printf("nope bro\n"); return -1;}

	if (argc == 3) {
		unsigned char* data2 = stbi_load(argv[2], &x, &y, &n, 3);
		if (!data2) {printf("nope bro\n"); return -1;}

		for (int i = 0; i < 80; i++) {
			for (int j = 0; j < 3; j++) {
				int a = data [i*3*136+j];
				int b = data2[i*3*136+j];

				if (a<b) {
					printf("+%x", b - a);
				} else if (a>b) {
					printf("-%x", a - b);
				} else {
					printf(" 0");
				}
				if (j == 2) printf("\n"); else printf(", ");
			}
		}

		stbi_image_free(data2);
	} else {

		for (int i = 0; i < 80; i++) {
			//printf("#%02x%02x%02x ", data[i*3*136+0], data[i*3*136+1], data[i*3*136+2]);
			//printf("(%03d,%03d,%03d) ", data[i*3*136+0], data[i*3*136+1], data[i*3*136+2]);
			printf("%d %d %d; ", data[i*3*136+2] % 10, data[i*3*136+1] % 10, data[i*3*136+0] % 10);
		}
	}

	stbi_image_free(data);
	return 0;
}