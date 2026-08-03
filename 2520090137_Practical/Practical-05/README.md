# Practical Experiment 05: Inter-Process Communication using Unnamed Pipes

## Aim
To establish unidirectional Inter-Process Communication (IPC) between parent and child processes using pipe().

## Source Code (`main.c`)
```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pipe(pipefd);
    pid_t pid = fork();

    if (pid == 0) {
        close(pipefd[1]);
        char buf[128];
        read(pipefd[0], buf, sizeof(buf));
        printf("[Consumer Child] Received data: %s\n", buf);
        close(pipefd[0]);
    } else {
        close(pipefd[0]);
        char msg[] = "OSSP Pipe IPC Data Payload";
        write(pipefd[1], msg, strlen(msg) + 1);
        close(pipefd[1]);
        printf("[Producer Parent] Sent data to pipe.\n");
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
[Producer Parent] Sent data to pipe.
[Consumer Child] Received data: OSSP Pipe IPC Data Payload
```

## OS & System Programming Concepts
An anonymous pipe creates a kernel-managed circular data buffer with read (pipefd[0]) and write (pipefd[1]) file descriptors shared across fork().
