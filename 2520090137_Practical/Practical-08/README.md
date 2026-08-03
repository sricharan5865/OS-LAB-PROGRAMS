# Practical Experiment 08: Dynamic Memory Allocation & Resizing

## Aim
To demonstrate heap dynamic memory allocation, resizing, and deallocation using malloc(), realloc(), and free().

## Source Code (`main.c`)
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int*)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i * 10;

    arr = (int*)realloc(arr, 10 * sizeof(int));
    for (int i = 5; i < 10; i++) arr[i] = i * 10;

    printf("Dynamically Resized Array: ");
    for (int i = 0; i < 10; i++) printf("%d ", arr[i]);
    printf("\n");

    free(arr);
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
Dynamically Resized Array: 0 10 20 30 40 50 60 70 80 90
```

## OS & System Programming Concepts
malloc() allocates contiguous uninitialized heap bytes, realloc() extends or relocates heap blocks, and free() returns memory to glibc allocator pool.
