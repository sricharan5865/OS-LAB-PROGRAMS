#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int data = 100;

int main() {
    printf("Before fork - Data: %d (Address: %p)\n", data, (void*)&data);
    if (fork() == 0) {
        printf("[Child Before Write] Data: %d (Addr: %p)\n", data, (void*)&data);
        data = 200; // Trigger Copy-On-Write
        printf("[Child After Write] Data: %d (Addr: %p)\n", data, (void*)&data);
    } else {
        wait(NULL);
        printf("[Parent] Data: %d (Addr: %p)\n", data, (void*)&data);
    }
    return 0;
}