#include <stdio.h>
#include <pthread.h>

pthread_mutex_t m1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t m2 = PTHREAD_MUTEX_INITIALIZER;

void* t1_func(void *arg) {
    (void)arg;
    pthread_mutex_lock(&m1);
    pthread_mutex_lock(&m2); // Resource ordering prevents deadlock
    printf("Thread 1 executed safely\n");
    pthread_mutex_unlock(&m2);
    pthread_mutex_unlock(&m1);
    return NULL;
}

void* t2_func(void *arg) {
    (void)arg;
    pthread_mutex_lock(&m1); // Ordered resource acquisition
    pthread_mutex_lock(&m2);
    printf("Thread 2 executed safely\n");
    pthread_mutex_unlock(&m2);
    pthread_mutex_unlock(&m1);
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_create(&t1, NULL, t1_func, NULL);
    pthread_create(&t2, NULL, t2_func, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    printf("Deadlock Prevention via Resource Ordering Succeeded.\n");
    return 0;
}