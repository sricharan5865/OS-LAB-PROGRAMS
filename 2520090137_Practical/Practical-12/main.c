#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_signal(int sig) {
    printf("Captured Signal %d\n", sig);
}

int main() {
    signal(SIGINT, handle_signal);
    signal(SIGTERM, handle_signal);
    signal(SIGUSR1, handle_signal);
    printf("Signal Handler Ready. PID: %d. Waiting for signals...\n", getpid());
    sleep(3);
    return 0;
}