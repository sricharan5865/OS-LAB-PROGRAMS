CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical5

all: $(TARGET)

$(TARGET): Practical5.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical5.c

clean:
	rm -f $(TARGET) *.o
