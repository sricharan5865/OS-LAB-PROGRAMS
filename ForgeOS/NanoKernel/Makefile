CC = gcc
CFLAGS = -Wall -Wextra -std=c99

all: nanokernel

nanokernel: kernel.c
	$(CC) $(CFLAGS) kernel.c -o nanokernel

clean:
	rm -f nanokernel *.o
