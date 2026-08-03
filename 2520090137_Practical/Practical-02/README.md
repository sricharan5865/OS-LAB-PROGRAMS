# Practical Experiment 02: File Copy Utility using Low-Level System Calls

## Aim
To create a file copy program in C utilizing UNIX low-level system calls open(), read(), write(), and close().

## Source Code (`main.c`)
```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

#define BUF_SIZE 1024

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <source> <destination>\n", argv[0]);
        return 1;
    }
    int src_fd = open(argv[1], O_RDONLY);
    if (src_fd < 0) { perror("Source file open failed"); return 1; }

    int dst_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (dst_fd < 0) { perror("Destination open failed"); close(src_fd); return 1; }

    char buffer[BUF_SIZE];
    ssize_t bytes_read;
    while ((bytes_read = read(src_fd, buffer, BUF_SIZE)) > 0) {
        write(dst_fd, buffer, bytes_read);
    }
    close(src_fd);
    close(dst_fd);
    printf("File copied successfully via low-level system calls.\n");
    return 0;
}
```

## Compilation & Execution
```bash
make
./main
```

## Execution Output
```text
$ gcc main.c -o copy_util
$ ./copy_util input.txt output.txt
File copied successfully via low-level system calls.
```

## OS & System Programming Concepts
Demonstrates direct interaction with the kernel VFS layer without standard I/O library buffering using open(), read(), write(), and close().
