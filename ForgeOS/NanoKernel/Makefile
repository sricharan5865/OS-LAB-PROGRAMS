CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = nanokernel

all: $(TARGET)

$(TARGET): kernel.c
	$(CC) $(CFLAGS) -o $(TARGET) kernel.c

clean:
	rm -f $(TARGET) *.o
