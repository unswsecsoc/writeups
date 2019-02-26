CC=gcc
VULN=-fno-stack-protector -no-pie

all: whropper

whropper :
	$(CC) $(VULN) -o whropper whropper.c

clean:
	rm -f whropper

