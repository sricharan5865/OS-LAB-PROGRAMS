#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int global_var = 100;
static int static_var = 200;

void show_addresses()
{
    int local_var = 300;
    printf("\n===== MEMORY ADDRESSES =====\n");
    printf("Code/Text address   : %p\n", (void *)show_addresses);
    printf("Global variable     : %p\n", (void *)&global_var);
    printf("Static variable     : %p\n", (void *)&static_var);

    int *heap_var = malloc(sizeof(int));
    if (heap_var == NULL)
    {
        printf("Heap allocation failed\n");
        return;
    }
    *heap_var = 400;

    printf("Heap variable       : %p\n", (void *)heap_var);
    printf("Stack variable      : %p\n", (void *)&local_var);
    printf("\nProcess ID (PID)    : %d\n", getpid());
    free(heap_var);
}

int main()
{
    show_addresses();

    printf("\nPress Enter to exit...\n");
    getchar();
    return 0;
}
