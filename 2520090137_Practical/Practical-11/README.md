# Practical Experiment 11: Multi-Threading & Concurrency Race Conditions

## Aim
To demonstrate concurrent thread creation using POSIX Threads (pthread) and observe race conditions on shared memory.

## Source Code (`main.c`)
```c
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
```

## Compilation & Execution
```bash
make
./main
```

## Execution Output
```text
Final Counter Value (Race Condition): 248912
(Expected: 400000. Counter mismatch due to un-synchronized concurrent access)
```

## OS & System Programming Concepts
Without mutual exclusion, multiple threads executing non-atomic read-modify-write CPU instructions on shared counter produce race conditions.
