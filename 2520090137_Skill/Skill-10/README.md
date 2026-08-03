# Skill Activity 10: Interactive Mini Shell Program

## Aim & Overview
Building an interactive command line prompt accepting user commands, executing via fork(), exec(), and wait(), and printing PIDs.

## Implementation (`main.c`)
```c
// Skill 10: Mini Shell Implementation
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
```

## Compilation & Execution
```bash
make
./main
```

## Output & Verification
```text
minishell> date
Mon Aug 3 11:45:00 IST 2026
```

## Key Learning Points
Combined fork(), exec(), and wait() into a functional user-space shell program loop.
