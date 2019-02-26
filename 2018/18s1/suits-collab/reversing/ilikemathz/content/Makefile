CC=gcc
VULN=-fno-stack-protector -no-pie

all: ilikemathz

ilikemathz :
	$(CC) $(VULN) -o ilikemathz ilikemathz.c

clean:
	rm -f ilikemathz

