CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical8

all: $(TARGET)

$(TARGET): Practical8.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical8.c

clean:
	rm -f $(TARGET) *.o
