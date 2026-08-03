CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical7

all: $(TARGET)

$(TARGET): Practical7.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical7.c

clean:
	rm -f $(TARGET) *.o
