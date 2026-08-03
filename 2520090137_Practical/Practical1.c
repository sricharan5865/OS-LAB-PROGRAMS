#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    char cmd[50];
    printf("Enter Linux Command: ");
    if (scanf("%49s", cmd) != 1) return 1;

    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        printf("\nChild Process\nChild PID : %d\nParent PID: %d\n", getpid(), getppid());
        execlp(cmd, cmd, NULL);
        perror("Command Execution Failed");
        exit(1);
    } else {
        printf("\nParent Process\nParent PID : %d\nChild PID  : %d\n", getpid(), pid);
        wait(NULL);
        printf("\nChild Process Completed\n");
    }
    return 0;
}