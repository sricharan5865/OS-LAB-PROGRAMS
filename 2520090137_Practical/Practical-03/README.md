# Practical Experiment 03: Process States & Lifecycle Inspection

## Aim
To observe and print process lifecycle states (Running, Waiting, Terminated) and track PID/PPID hierarchy.

## Source Code (`main.c`)
```c
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    printf("[State: Running] Parent Process PID: %d, PPID: %d\n", getpid(), getppid());
    pid_t pid = fork();
    if (pid == 0) {
        printf("[State: Running] Child Process PID: %d, PPID: %d\n", getpid(), getppid());
        sleep(1);
        printf("[State: Terminating] Child exiting.\n");
    } else {
        printf("[State: Waiting] Parent waiting for child PID: %d\n", pid);
        wait(NULL);
        printf("[State: Terminated] Parent completed child join.\n");
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
[State: Running] Parent Process PID: 4050, PPID: 1200
[State: Waiting] Parent waiting for child PID: 4051
[State: Running] Child Process PID: 4051, PPID: 4050
[State: Terminating] Child exiting.
[State: Terminated] Parent completed child join.
```

## OS & System Programming Concepts
Illustrates process transitions across Ready, Running, Waiting (blocked on wait), and Terminated states in the Linux PCB (Process Control Block).
