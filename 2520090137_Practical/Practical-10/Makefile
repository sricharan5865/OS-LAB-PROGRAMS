CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical10

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

clean:
	rm -f $(TARGET) *.o
