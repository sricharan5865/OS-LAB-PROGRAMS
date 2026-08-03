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