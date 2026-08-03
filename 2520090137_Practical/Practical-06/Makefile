CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = practical06

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

clean:
	rm -f $(TARGET) *.o
