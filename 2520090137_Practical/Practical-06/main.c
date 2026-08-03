#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Running process for state monitoring. PID: %d\n", getpid());
    printf("Check process status: cat /proc/%d/status\n", getpid());
    sleep(10);
    return 0;
}