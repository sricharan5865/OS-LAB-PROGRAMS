#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

int main() {
    int fd = open("mmap_test.txt", O_RDWR | O_CREAT | O_TRUNC, 0644);
    write(fd, "Memory-Mapped I/O Content", 25);

    char *map = mmap(NULL, 25, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    printf("Mapped File Content: %s\n", map);
    munmap(map, 25);
    close(fd);
    return 0;
}