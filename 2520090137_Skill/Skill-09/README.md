# Skill Activity 09: System Call Tracing using strace

## Aim & Overview
Tracing Linux binaries (ls, pwd, date) using strace, observing execve(), openat(), read(), write(), and close() system call sequences.

## Implementation (`main.c`)
```c
// Skill 09: System Call Tracing
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Tracing system calls for process PID: %d\n", getpid());
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
$ strace ./main
execve("./main", ["./main"], 0x7ffc...) = 0
brk(NULL) = 0x55b1c000
write(1, "Tracing system calls...", 42) = 42
exit_group(0) = ?
```

## Key Learning Points
Used strace diagnostic utility to intercept and log kernel system call invocations.
