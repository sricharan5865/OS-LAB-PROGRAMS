CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical1

all: $(TARGET)

$(TARGET): Practical1.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical1.c

clean:
	rm -f $(TARGET) *.o
