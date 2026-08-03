# Skill Activity 07: Parent-Child Synchronization using wait() and waitpid()

## Aim & Overview
Implementing parent process blocking, child status collection, exit status evaluation, and termination synchronization.

## Implementation (`main.c`)
```c
// Skill 07: Parent-Child Synchronization using wait()
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        printf("[Child] Executing work...\n");
    } else {
        wait(NULL);
        printf("[Parent] Child terminated. Parent resuming.\n");
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
[Child] Executing work...
[Parent] Child terminated. Parent resuming.
```

## Key Learning Points
Demonstrated synchronous process coordination preventing orphan and zombie states.
