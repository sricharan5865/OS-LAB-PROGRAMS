CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical12

all: $(TARGET)

$(TARGET): Practical12.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical12.c

clean:
	rm -f $(TARGET) *.o
