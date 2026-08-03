#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    printf("[State: Running] Parent Process PID: %d, PPID: %d\n", getpid(), getppid());
    pid_t pid = fork();
    if (pid == 0) {
        printf("[State: Running] Child Process PID: %d, PPID: %d\n", getpid(), getppid());
        sleep(1);
        printf("[State: Terminating] Child exiting.\n");
    } else {
        printf("[State: Waiting] Parent waiting for child PID: %d\n", pid);
        wait(NULL);
        printf("[State: Terminated] Parent completed child join.\n");
    }
    return 0;
}