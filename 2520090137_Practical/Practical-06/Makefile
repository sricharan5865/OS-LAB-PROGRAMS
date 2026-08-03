CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical6

all: $(TARGET)

$(TARGET): Practical6.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical6.c

clean:
	rm -f $(TARGET) *.o
