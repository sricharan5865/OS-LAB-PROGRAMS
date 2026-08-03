# Practical Experiment 10: File Metadata & Inode Structure Inspection

## Aim
To inspect file attributes, inode numbers, and hard link counts using the stat() system call.

## Source Code (`main.c`)
```c
#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>

int main() {
    struct stat st;
    if (stat("main.c", &st) == 0) {
        printf("File: main.c, Inode: %lu, Links: %lu, Size: %ld bytes\n", st.st_ino, st.st_nlink, st.st_size);
    }
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
File: main.c, Inode: 14298512, Links: 1, Size: 244 bytes
```

## OS & System Programming Concepts
Inodes hold filesystem metadata including permissions, ownership, timestamp, size, and data block pointers without storing the filename.
