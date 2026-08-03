// Project 2: NanoKernel (Kernel Space Simulation)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum { READY, RUNNING, BLOCKED, TERMINATED } ProcessState;

typedef struct {
    int pid;
    char name[32];
    ProcessState state;
    int priority;
} PCB;

void schedule_next(PCB processes[], int count) {
    printf("[NanoKernel Scheduler] Dispatching Process Tasks:\n");
    for (int i = 0; i < count; i++) {
        processes[i].state = RUNNING;
        printf(" -> Dispatching PID %d (%s) Priority %d\n", processes[i].pid, processes[i].name, processes[i].priority);
        processes[i].state = TERMINATED;
    }
}

int main() {
    printf("=== NanoKernel v1.0 Initialization ===\n");
    PCB table[3] = {
        {101, "init_task", READY, 1},
        {102, "vfs_service", READY, 2},
        {103, "net_daemon", READY, 3}
    };
    schedule_next(table, 3);
    printf("=== NanoKernel Scheduler Execution Finished ===\n");
    return 0;
}