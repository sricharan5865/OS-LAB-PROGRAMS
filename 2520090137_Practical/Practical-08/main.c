#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        printf("[Child] Exiting to become zombie... PID: %d\n", getpid());
        exit(0);
    } else {
        printf("[Parent] Sleeping for 5s without wait(). Check ps aux | grep 'Z'\n");
        sleep(5);
        wait(NULL);
        printf("[Parent] Reaped child zombie. Clean exit.\n");
    }
    return 0;
}