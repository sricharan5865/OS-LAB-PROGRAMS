# Practical Experiment 06: Inter-Process Communication using Named Pipes (FIFO)

## Aim
To implement IPC between unrelated processes using a Named Pipe (FIFO) created with mkfifo().

## Source Code (`main.c`)
```c
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
```

## Compilation & Execution
```bash
make
./main
```

## Execution Output
```text
FIFO created successfully at /tmp/my_fifo
$ ls -l /tmp/my_fifo
prw-r--r-- 1 student student 0 Aug 3 11:30 /tmp/my_fifo
```

## OS & System Programming Concepts
Named pipes (FIFOs) exist as special files in the filesystem, permitting IPC between processes without a common parent hierarchy.
