CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical11

all: $(TARGET)

$(TARGET): Practical11.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical11.c

clean:
	rm -f $(TARGET) *.o
