# Skill Activity 06: Process Replacement using the exec() Family

## Aim & Overview
Understanding process image replacement using execl(), execv(), execvp() family to replace process code, stack, and data.

## Implementation (`main.c`)
```c
// Skill 06: Process Replacement using exec() family
#include <stdio.h>
#include <unistd.h>

int main() {
    char *args[] = {"ls", "-l", NULL};
    printf("Executing ls via execvp...\n");
    execvp(args[0], args);
    perror("execvp failed");
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
Executing ls via execvp...
total 32
-rw-r--r-- 1 student student  263 Aug 3 11:40 main.c
-rw-r--r-- 1 student student  200 Aug 3 11:40 Makefile
```

## Key Learning Points
execvp() replaces current execution context with new program binary while preserving PID.
