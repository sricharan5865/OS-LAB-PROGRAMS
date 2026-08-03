#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void) {
    printf("[Parent] Process starting (PID: %d)\n", getpid());

    pid_t pid = fork();

    if (pid < 0) {
        perror("Fork failed");
        return EXIT_FAILURE;
    } else if (pid == 0) {
        // Child Process
        printf("[Child] Executing child process (PID: %d, Parent PID: %d)\n", getpid(), getppid());
        char *args[] = {"/bin/ls", "-l", NULL};
        execvp(args[0], args);
        perror("Exec failed");
        exit(EXIT_FAILURE);
    } else {
        // Parent Process
        int status;
        printf("[Parent] Waiting for child (PID: %d) to finish...\n", pid);
        waitpid(pid, &status, 0);
        if (WIFEXITED(status)) {
            printf("[Parent] Child exited with status code %d\n", WEXITSTATUS(status));
        }
    }

    return EXIT_SUCCESS;
}
