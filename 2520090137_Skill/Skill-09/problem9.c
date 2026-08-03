// 9. System Call Tracing
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Tracing system calls for process PID: %d\n", getpid());
    return 0;
}