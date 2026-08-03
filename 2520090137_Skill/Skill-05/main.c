// Skill 05: Process Creation using fork()
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Parent PID: %d\n", getpid());
    pid_t pid = fork();
    if (pid == 0) {
        printf("Child process PID: %d, Parent PID: %d\n", getpid(), getppid());
    }
    return 0;
}