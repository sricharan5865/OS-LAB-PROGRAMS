// Project 1: Shellforge (User Space Unix Shell)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

#define MAX_LINE 1024
#define MAX_ARGS 64

void execute_cmd(char **args) {
    if (args[0] == NULL) return;
    if (strcmp(args[0], "cd") == 0) {
        if (args[1] == NULL) chdir(getenv("HOME"));
        else if (chdir(args[1]) != 0) perror("cd failed");
        return;
    }
    if (strcmp(args[0], "exit") == 0) {
        exit(0);
    }
    pid_t pid = fork();
    if (pid == 0) {
        execvp(args[0], args);
        perror("Shellforge execution failed");
        exit(1);
    } else if (pid > 0) {
        wait(NULL);
    } else {
        perror("Fork failed");
    }
}

int main() {
    char line[MAX_LINE];
    char *args[MAX_ARGS];

    while (1) {
        printf("Shellforge: %s$ ", getcwd(NULL, 0));
        fflush(stdout);
        if (!fgets(line, sizeof(line), stdin)) break;

        line[strcspn(line, "\n")] = 0;
        int i = 0;
        char *token = strtok(line, " ");
        while (token != NULL && i < MAX_ARGS - 1) {
            args[i++] = token;
            token = strtok(NULL, " ");
        }
        args[i] = NULL;
        execute_cmd(args);
    }
    return 0;
}