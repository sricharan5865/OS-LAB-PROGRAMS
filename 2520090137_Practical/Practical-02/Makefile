CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical2

all: $(TARGET)

$(TARGET): Practical2.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical2.c

clean:
	rm -f $(TARGET) *.o
