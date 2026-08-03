CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = shellforge

all: $(TARGET)

$(TARGET): shell.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

clean:
	rm -f $(TARGET) *.o
