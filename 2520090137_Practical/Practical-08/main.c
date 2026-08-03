#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int*)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i * 10;

    arr = (int*)realloc(arr, 10 * sizeof(int));
    for (int i = 5; i < 10; i++) arr[i] = i * 10;

    for (int i = 0; i < 10; i++) printf("%d ", arr[i]);
    printf("\n");

    free(arr);
    return 0;
}