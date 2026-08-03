// 10. Mini Shell Program
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    char cmd[64];
    printf("minishell> ");
    if (scanf("%63s", cmd) == 1) {
        if (strcmp(cmd, "exit") == 0) return 0;
        pid_t pid = fork();
        if (pid == 0) {
            execlp(cmd, cmd, NULL);
            perror("Execution failed");
            exit(1);
        } else {
            wait(NULL);
        }
    }
    return 0;
}