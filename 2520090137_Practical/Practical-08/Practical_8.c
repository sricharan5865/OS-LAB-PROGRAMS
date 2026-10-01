#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;

    // 1. malloc()
    int *arr = (int *)malloc(5 * sizeof(int));

    if (arr == NULL)
    {
        printf("malloc failed!\n");
        return 1;
    }

    printf("Memory allocated using malloc()\n");

    for (i = 0; i < 5; i++)
    {
        arr[i] = (i + 1) * 10;
    }

    printf("malloc array: ");
    for (i = 0; i < 5; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // 2. calloc()
    int *zero_arr = (int *)calloc(5, sizeof(int));

    if (zero_arr == NULL)
    {
        printf("calloc failed!\n");
        free(arr);
        return 1;
    }

    printf("\nMemory allocated using calloc()\n");

    printf("calloc array: ");
    for (i = 0; i < 5; i++)
    {
        printf("%d ", zero_arr[i]);
    }
    printf("\n");

    // 3. realloc()
    arr = (int *)realloc(arr, 10 * sizeof(int));

    if (arr == NULL)
    {
        printf("realloc failed!\n");
        free(zero_arr);
        return 1;
    }

    printf("\nMemory resized using realloc()\n");

    for (i = 5; i < 10; i++)
    {
        arr[i] = (i + 1) * 10;
    }

    printf("After realloc: ");
    for (i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // 4. free()
    free(arr);
    free(zero_arr);

    printf("\nMemory released using free()\n");

    return 0;
}
