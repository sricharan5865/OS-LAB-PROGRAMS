#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Inspect virtual memory map using: cat /proc/%d/maps\n", getpid());
    return 0;
}