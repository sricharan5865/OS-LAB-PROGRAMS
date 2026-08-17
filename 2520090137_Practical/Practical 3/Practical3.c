#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {

    pid_t pid = fork();

    if (pid < 0) {
        perror("Fork failed");
        return 1;
    }

    if (pid == 0) {

        printf("[Running] Child Process\n");
        printf("Child PID  : %d\n", getpid());
        printf("Child PPID : %d\n", getppid());

        printf("[Waiting] Child sleeping for 10 seconds...\n");
        sleep(10);

        printf("[Running] Child resumed\n");

        printf("[Terminating] Child exiting...\n");
        return 0;

    } else {

        printf("[Running] Parent Process\n");
        printf("Parent PID : %d\n", getpid());
        printf("Parent PPID: %d\n", getppid());
        printf("Child PID  : %d\n", pid);

        printf("[Waiting] Parent waiting for child...\n");

        wait(NULL);

        printf("[Running] Child completed.\n");
        printf("[Terminated] Parent completed.\n");
    }

    return 0;
