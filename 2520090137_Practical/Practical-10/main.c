#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>

int main() {
    struct stat st;
    if (stat("main.c", &st) == 0) {
        printf("File: main.c, Inode: %lu, Links: %lu\n", st.st_ino, st.st_nlink);
    }
    return 0;
}