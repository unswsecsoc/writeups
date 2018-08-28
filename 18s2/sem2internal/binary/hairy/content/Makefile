CC=gcc
FLAGS=-w -O0 -ggdb -D_FORTIFY_SOURCE=0 -Wno-format -Wno-format-security

all: hairy

hairy:
	$(CC) $(FLAGS) -o hairy hairy.c

clean:
	rm -rf hairy
