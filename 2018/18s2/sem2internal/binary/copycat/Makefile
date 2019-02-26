CC=gcc
FLAGS=-w -O0 -ggdb -D_FORTIFY_SOURCE=0 -Wno-format -Wno-format-security

all: copycat

hairy:
	$(CC) $(FLAGS) -o copycat copycat.c

clean:
	rm -rf copycat
