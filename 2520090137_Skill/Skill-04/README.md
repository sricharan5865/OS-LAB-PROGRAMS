# Skill Activity 04: Shell Architecture & Makefile Automation

## Aim & Overview
Understanding User -> Shell -> Kernel -> Hardware architecture layers, process execution flow, and writing automated build Makefiles.

## Implementation (`main.c`)
```c
// Skill 04: Shell Architecture & Makefile Automation
#include <stdio.h>

int main() {
    printf("Build automation via Makefile executed successfully.\n");
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
$ make clean
rm -f main *.o
$ make
gcc -Wall -Wextra -std=c99 main.c -o main
$ ./main
Build automation via Makefile executed successfully.
```

## Key Learning Points
Built modular Makefile targets (all, clean, run) to automate C compilation workflows.
