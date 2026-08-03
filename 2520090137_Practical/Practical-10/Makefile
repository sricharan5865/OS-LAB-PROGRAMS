CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical10

all: $(TARGET)

$(TARGET): Practical10.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical10.c

clean:
	rm -f $(TARGET) *.o
