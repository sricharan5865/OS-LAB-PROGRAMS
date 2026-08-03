#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t p1 = fork();
    if (p1 == 0) {
        sleep(2);
        printf("Child 1 (PID: %d) exiting\n", getpid());
        exit(10);
    }
    pid_t p2 = fork();
    if (p2 == 0) {
        sleep(1);
        printf("Child 2 (PID: %d) exiting\n", getpid());
        exit(20);
    }

    int status;
    waitpid(p2, &status, 0);
    printf("Parent joined Child 2 first via waitpid. Exit status: %d\n", WEXITSTATUS(status));

    wait(&status);
    printf("Parent joined remaining Child 1 via wait. Exit status: %d\n", WEXITSTATUS(status));
    return 0;
}