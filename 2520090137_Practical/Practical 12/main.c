#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

sem_t empty, full;

void* producer(void *arg) {
    (void)arg;
    sem_wait(&empty);
    printf("[Producer] Produced Item\n");
    sem_post(&full);
    return NULL;
}

void* consumer(void *arg) {
    (void)arg;
    sem_wait(&full);
    printf("[Consumer] Consumed Item\n");
    sem_post(&empty);
    return NULL;
}

int main() {
    pthread_t t1, t2;
    sem_init(&empty, 0, 1);
    sem_init(&full, 0, 0);

    pthread_create(&t1, NULL, producer, NULL);
    pthread_create(&t2, NULL, consumer, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    sem_destroy(&empty);
    sem_destroy(&full);
    return 0;
}