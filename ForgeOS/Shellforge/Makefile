CC = gcc
CFLAGS = -Wall -Wextra -std=c99

all: shellforge

shellforge: shell.c
	$(CC) $(CFLAGS) shell.c -o shellforge

clean:
	rm -f shellforge *.o
