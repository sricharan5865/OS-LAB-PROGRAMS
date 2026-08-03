CC = gcc
CFLAGS = -Wall -Wextra -std=c99

all: main

main: main.c
	$(CC) $(CFLAGS) main.c -o main

clean:
	rm -f main *.o

run: main
	./main
