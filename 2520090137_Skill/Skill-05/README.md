# Skill Activity 05: Process Creation using fork()

## Aim & Overview
Exploring process abstraction, fork() system call mechanics, parent and child process execution, PID/PPID retrieval.

## Implementation (`main.c`)
```c
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
```

## Compilation & Execution
```bash
make
./main
```

## Output & Verification
```text
Parent PID: 6100
Child process PID: 6101, Parent PID: 6100
```

## Key Learning Points
Analyzed kernel PCB clone mechanism and address space duplication upon calling fork().
