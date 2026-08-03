#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
    char *fifo = "/tmp/my_fifo";
    mkfifo(fifo, 0666);
    printf("FIFO created successfully at %s\n", fifo);
    return 0;
}