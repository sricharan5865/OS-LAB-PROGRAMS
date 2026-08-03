CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical9

all: $(TARGET)

$(TARGET): Practical9.c
	$(CC) $(CFLAGS) -o $(TARGET) Practical9.c

clean:
	rm -f $(TARGET) *.o
