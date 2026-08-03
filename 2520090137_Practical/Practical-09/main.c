#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("test_low.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    write(fd, "Low-level system call I/O\n", 26);
    close(fd);

    FILE *f = fopen("test_std.txt", "w");
    fputs("Standard library buffered I/O\n", f);
    fclose(f);

    printf("I/O Comparison completed.\n");
    return 0;
}