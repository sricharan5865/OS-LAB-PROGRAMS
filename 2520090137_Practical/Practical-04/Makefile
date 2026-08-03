CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical4

all: $(TARGET)

$(TARGET): Practical4.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical4.c

clean:
	rm -f $(TARGET) *.o
