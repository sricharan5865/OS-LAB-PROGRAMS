#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAX_LINE 1024
#define MAX_ARGS 64

int shell_cd(char **args) {
    if (args[1] == NULL) {
        fprintf(stderr, "shellforge: expected argument to \"cd\"\n");
    } else {
        if (chdir(args[1]) != 0) {
            perror("shellforge");
        }
    }
    return 1;
}

int shell_help(char **args) {
    (void)args;
    printf("=== Shellforge (ForgeOS User Space Shell) ===\n");
    printf("Type program names and arguments, then hit enter.\n");
    printf("Built-in commands:\n");
    printf("  cd <path>  - Change current directory\n");
    printf("  help       - Display help screen\n");
    printf("  exit       - Terminate shellforge\n");
    return 1;
}

int shell_exit(char **args) {
    (void)args;
    return 0;
}

int launch_process(char **args) {
    pid_t pid = fork();
    if (pid == 0) {
        if (execvp(args[0], args) == -1) {
            perror("shellforge");
        }
        exit(EXIT_FAILURE);
    } else if (pid < 0) {
        perror("shellforge: fork failed");
    } else {
        int status;
        do {
            waitpid(pid, &status, WUNTRACED);
        } while (!WIFEXITED(status) && !WIFSIGNALED(status));
    }
    return 1;
}

int execute(char **args) {
    if (args[0] == NULL) return 1;

    if (strcmp(args[0], "cd") == 0) return shell_cd(args);
    if (strcmp(args[0], "help") == 0) return shell_help(args);
    if (strcmp(args[0], "exit") == 0) return shell_exit(args);

    return launch_process(args);
}

void prompt(void) {
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("shellforge:%s$ ", cwd);
    } else {
        printf("shellforge$ ");
    }
    fflush(stdout);
}

int main(void) {
    char line[MAX_LINE];
    char *args[MAX_ARGS];
    int status = 1;

    while (status) {
        prompt();
        if (!fgets(line, sizeof(line), stdin)) break;

        line[strcspn(line, "\n")] = 0;
        int i = 0;
        char *token = strtok(line, " \t");
        while (token != NULL && i < MAX_ARGS - 1) {
            args[i++] = token;
            token = strtok(NULL, " \t");
        }
        args[i] = NULL;

        status = execute(args);
    }

    return EXIT_SUCCESS;
}
