#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 4
#define ITERATIONS 10000

long counter = 0;
pthread_mutex_t lock;

void *count_words(void *arg) {
    long thread_id = (long)arg;
    for (int i = 0; i < ITERATIONS; i++) {
        pthread_mutex_lock(&lock);
        counter++;
        pthread_mutex_unlock(&lock);
    }
    printf("[Thread %ld] Completed increment loop\n", thread_id);
    pthread_exit(NULL);
}

int main(void) {
    pthread_t threads[NUM_THREADS];
    pthread_mutex_init(&lock, NULL);

    for (long i = 0; i < NUM_THREADS; i++) {
        if (pthread_create(&threads[i], NULL, count_words, (void *)i) != 0) {
            perror("Thread creation failed");
            return EXIT_FAILURE;
        }
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&lock);
    printf("Final synchronized counter value: %ld (Expected: %d)\n", counter, NUM_THREADS * ITERATIONS);
    return EXIT_SUCCESS;
}
