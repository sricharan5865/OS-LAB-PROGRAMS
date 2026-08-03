# Practical Experiment 09: Low-Level vs Buffered I/O Performance & Mechanics

## Aim
To compare unbuffered low-level system call I/O (write) with C standard library buffered I/O (fputs).

## Source Code (`main.c`)
```c
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
```

## Compilation & Execution
```bash
make
./main
```

## Execution Output
```text
I/O Comparison completed.
$ cat test_low.txt
Low-level system call I/O
$ cat test_std.txt
Standard library buffered I/O
```

## OS & System Programming Concepts
Unbuffered write() incurs kernel context switches per call, while standard FILE* stream buffering aggregates user-space data before calling write().
