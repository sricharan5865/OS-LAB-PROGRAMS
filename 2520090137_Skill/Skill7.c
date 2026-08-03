// 7. Parent-Child Synchronization using wait()
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        printf("[Child] Executing work...\n");
    } else {
        wait(NULL);
        printf("[Parent] Child terminated. Parent resuming.\n");
    }
    return 0;
}