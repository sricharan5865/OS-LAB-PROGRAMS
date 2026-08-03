CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical3

all: $(TARGET)

$(TARGET): Practical3.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical3.c

clean:
	rm -f $(TARGET) *.o
