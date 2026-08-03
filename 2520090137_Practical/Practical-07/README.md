# Practical Experiment 07: Process Memory Layout & Address Space Inspection

## Aim
To inspect the memory addresses of code (text), global (data), static (BSS), heap, and stack variables in a process.

## Source Code (`main.c`)
```c
#include <stdio.h>
#include <stdlib.h>

int global_var = 10;
static int static_var = 20;

int main() {
    int stack_var = 30;
    int *heap_var = (int*)malloc(sizeof(int));
    *heap_var = 40;

    printf("Code (main)      : %p\n", (void*)main);
    printf("Global Variable  : %p\n", (void*)&global_var);
    printf("Static Variable  : %p\n", (void*)&static_var);
    printf("Heap Allocation  : %p\n", (void*)heap_var);
    printf("Stack Variable   : %p\n", (void*)&stack_var);

    free(heap_var);
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
Code (main)      : 0x55a2b104a119
Global Variable  : 0x55a2b104c010
Static Variable  : 0x55a2b104c014
Heap Allocation  : 0x55a2b21fe2a0
Stack Variable   : 0x7ffd9c34a2ec
```

## OS & System Programming Concepts
Verifies virtual address organization: Text/Code at low memory, Data/BSS above, Heap growing upward, and Stack growing downward from high memory.
