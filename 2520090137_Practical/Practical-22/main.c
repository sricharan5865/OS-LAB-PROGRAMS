#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
long counter = 0;
pthread_mutex_t lock;

void* count_func(void *arg) {
    (void)arg;
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&lock);
        counter++;
        pthread_mutex_unlock(&lock);
    }
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];
    pthread_mutex_init(&lock, NULL);
    for (int i = 0; i < NUM_THREADS; i++) pthread_create(&threads[i], NULL, count_func, NULL);
    for (int i = 0; i < NUM_THREADS; i++) pthread_join(threads[i], NULL);
    pthread_mutex_destroy(&lock);
    printf("Final Synchronized Counter Value: %ld\n", counter);
    return 0;
}