# Practical Experiment 04: Parent-Child Synchronization via waitpid()

## Aim
To demonstrate selective parent waiting and synchronization with specific child processes using waitpid().

## Source Code (`main.c`)
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t p1 = fork();
    if (p1 == 0) { sleep(2); printf("Child 1 (PID: %d) exiting\n", getpid()); exit(10); }

    pid_t p2 = fork();
    if (p2 == 0) { sleep(1); printf("Child 2 (PID: %d) exiting\n", getpid()); exit(20); }

    int status;
    waitpid(p2, &status, 0);
    printf("Parent joined Child 2 first via waitpid. Exit status: %d\n", WEXITSTATUS(status));

    wait(&status);
    printf("Parent joined remaining Child 1 via wait. Exit status: %d\n", WEXITSTATUS(status));
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
Child 2 (PID: 5122) exiting
Parent joined Child 2 first via waitpid. Exit status: 20
Child 1 (PID: 5121) exiting
Parent joined remaining Child 1 via wait. Exit status: 10
```

## OS & System Programming Concepts
waitpid() enables non-blocking or out-of-order process harvesting by targeting a specific child PID, preventing zombie process accumulation.
