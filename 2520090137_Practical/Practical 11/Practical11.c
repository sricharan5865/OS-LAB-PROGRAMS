#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
long counter = 0;

void* count_func(void *arg) {
    (void)arg;
    for (int i = 0; i < 100000; i++) counter++;
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];
    for (int i = 0; i < NUM_THREADS; i++) pthread_create(&threads[i], NULL, count_func, NULL);
    for (int i = 0; i < NUM_THREADS; i++) pthread_join(threads[i], NULL);
    printf("Final Counter Value (Race Condition): %ld\n", counter);
    return 0;
}