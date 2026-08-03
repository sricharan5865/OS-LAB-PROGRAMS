// 8. Process Tree Analysis
#include <stdio.h>
#include <unistd.h>

int main() {
    fork();
    fork();
    printf("Process PID: %d, Parent PID: %d\n", getpid(), getppid());
    return 0;
}