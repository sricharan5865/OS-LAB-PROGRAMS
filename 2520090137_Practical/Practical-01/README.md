# Practical Experiment 01: Hardware Resources & OS Abstraction

## Aim
To study how the operating system abstracts hardware resources (CPU, memory, storage, I/O devices) using Linux commands and demonstrate process creation using fork(), exec(), and wait().

## Source Code (`main.c`)
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    char cmd[50];
    printf("Enter Linux Command: ");
    if (scanf("%49s", cmd) != 1) return 1;

    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        printf("\nChild Process\nChild PID : %d\nParent PID: %d\n", getpid(), getppid());
        execlp(cmd, cmd, NULL);
        perror("Command Execution Failed");
        exit(1);
    } else {
        printf("\nParent Process\nParent PID : %d\nChild PID  : %d\n", getpid(), pid);
        wait(NULL);
        printf("\nChild Process Completed\n");
    }
    return 0;
}
```

## Compilation & Execution
```bash
make
./main
```

## Execution Output
```text
Enter Linux Command: ls
Parent Process
Parent PID : 1876
Child PID  : 1877

Child Process
Child PID : 1877
Parent PID: 1876
main.c Makefile Practical-01_Report.docx README.md

Child Process Completed
```

## OS & System Programming Concepts
The OS abstracts CPU execution via process scheduling. fork() duplicates the calling process into a parent and child. exec() replaces the child's address space with the requested program, and wait() blocks the parent until the child terminates.
