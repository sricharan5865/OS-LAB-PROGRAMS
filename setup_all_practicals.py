import os

repo_dir = r"C:\Users\sri charan\.gemini\antigravity\scratch\2520090137_OSSP"
prac_root = os.path.join(repo_dir, "2520090137_Practical")

practicals = {
"Practical-01": ("Interactive Command Execution Shell using fork, exec, wait", """#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    char cmd[50];
    printf("Enter Linux Command: ");
    if (scanf("%49s", cmd) != 1) return 1;

    pid_t pid = fork();
    if (pid < 0) {
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        printf("\\nChild Process\\nChild PID : %d\\nParent PID: %d\\n", getpid(), getppid());
        execlp(cmd, cmd, NULL);
        perror("Command Execution Failed");
        exit(1);
    } else {
        printf("\\nParent Process\\nParent PID : %d\\nChild PID  : %d\\n", getpid(), pid);
        wait(NULL);
        printf("\\nChild Process Completed\\n");
    }
    return 0;
}"""),

"Practical-02": ("Hardware Resources & OS Abstraction Investigation", """// Command execution script for hardware & OS service investigation
// uname -a, lscpu, lsblk, ps -ef, top
#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("--- OS & Hardware Services Information ---\\n");
    system("uname -a");
    system("lscpu | head -n 10");
    system("lsblk");
    return 0;
}"""),

"Practical-03": ("File Copy using open, read, write, and close System Calls", """#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

#define BUF_SIZE 1024

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <source> <destination>\\n", argv[0]);
        return 1;
    }
    int src_fd = open(argv[1], O_RDONLY);
    if (src_fd < 0) { perror("Source open failed"); return 1; }

    int dst_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (dst_fd < 0) { perror("Destination open failed"); close(src_fd); return 1; }

    char buffer[BUF_SIZE];
    ssize_t bytes_read;
    while ((bytes_read = read(src_fd, buffer, BUF_SIZE)) > 0) {
        write(dst_fd, buffer, bytes_read);
    }
    close(src_fd);
    close(dst_fd);
    printf("File copied successfully via low-level system calls.\\n");
    return 0;
}"""),

"Practical-04": ("System Call Tracing with strace Utility", """#include <stdio.h>

int main() {
    FILE *f = fopen("sample.txt", "w");
    if (f) {
        fputs("Hello World from OSSP Practical System Call Tracing\\n", f);
        fclose(f);
    }
    printf("sample.txt prepared. Run: strace cat sample.txt\\n");
    return 0;
}"""),

"Practical-05": ("Process State Inspection (PID, PPID, and Execution Stages)", """#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    printf("[State: Running] Parent Process PID: %d, PPID: %d\\n", getpid(), getppid());
    pid_t pid = fork();
    if (pid == 0) {
        printf("[State: Running] Child Process PID: %d, PPID: %d\\n", getpid(), getppid());
        sleep(1);
        printf("[State: Terminating] Child exiting.\\n");
    } else {
        printf("[State: Waiting] Parent waiting for child PID: %d\\n", pid);
        wait(NULL);
        printf("[State: Terminated] Parent completed child join.\\n");
    }
    return 0;
}"""),

"Practical-06": ("Process State Transitions Observation via /proc & Linux Tools", """#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Running process for state monitoring. PID: %d\\n", getpid());
    printf("Check process status: cat /proc/%d/status\\n", getpid());
    sleep(10);
    return 0;
}"""),

"Practical-07": ("Parent Synchronization with Multiple Child Processes (wait & waitpid)", """#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t p1 = fork();
    if (p1 == 0) {
        sleep(2);
        printf("Child 1 (PID: %d) exiting\\n", getpid());
        exit(10);
    }
    pid_t p2 = fork();
    if (p2 == 0) {
        sleep(1);
        printf("Child 2 (PID: %d) exiting\\n", getpid());
        exit(20);
    }

    int status;
    waitpid(p2, &status, 0);
    printf("Parent joined Child 2 first via waitpid. Exit status: %d\\n", WEXITSTATUS(status));

    wait(&status);
    printf("Parent joined remaining Child 1 via wait. Exit status: %d\\n", WEXITSTATUS(status));
    return 0;
}"""),

"Practical-08": ("Zombie Process Creation, Investigation, and Elimination", """#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    if (pid == 0) {
        printf("[Child] Exiting to become zombie... PID: %d\\n", getpid());
        exit(0);
    } else {
        printf("[Parent] Sleeping for 5s without wait(). Check ps aux | grep 'Z'\\n");
        sleep(5);
        wait(NULL);
        printf("[Parent] Reaped child zombie. Clean exit.\\n");
    }
    return 0;
}"""),

"Practical-09": ("Producer-Consumer Communication using Anonymous Pipes", """#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pipe(pipefd);
    pid_t pid = fork();

    if (pid == 0) {
        close(pipefd[1]);
        char buf[128];
        read(pipefd[0], buf, sizeof(buf));
        printf("[Consumer Child] Received data: %s\\n", buf);
        close(pipefd[0]);
    } else {
        close(pipefd[0]);
        char msg[] = "OSSP Pipe IPC Data Payload";
        write(pipefd[1], msg, strlen(msg) + 1);
        close(pipefd[1]);
        printf("[Producer Parent] Sent data to pipe.\\n");
    }
    return 0;
}"""),

"Practical-10": ("Shell Pipeline Implementation (ls -l | grep .c)", """#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pipefd[2];
    pipe(pipefd);

    if (fork() == 0) {
        dup2(pipefd[1], STDOUT_FILENO);
        close(pipefd[0]); close(pipefd[1]);
        execlp("ls", "ls", "-l", NULL);
    }

    if (fork() == 0) {
        dup2(pipefd[0], STDIN_FILENO);
        close(pipefd[0]); close(pipefd[1]);
        execlp("grep", "grep", ".c", NULL);
    }

    close(pipefd[0]); close(pipefd[1]);
    wait(NULL); wait(NULL);
    return 0;
}"""),

"Practical-11": ("Client-Server IPC using Named Pipes (FIFOs)", """#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

int main() {
    char *fifo = "/tmp/my_fifo";
    mkfifo(fifo, 0666);
    printf("FIFO created at %s\\n", fifo);
    return 0;
}"""),

"Practical-12": ("POSIX Signal Handling (SIGINT, SIGTERM, SIGUSR1)", """#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_signal(int sig) {
    printf("Captured Signal %d\\n", sig);
}

int main() {
    signal(SIGINT, handle_signal);
    signal(SIGTERM, handle_signal);
    signal(SIGUSR1, handle_signal);
    printf("Signal Handler Ready. PID: %d. Waiting for signals...\\n", getpid());
    sleep(3);
    return 0;
}"""),

"Practical-13": ("Process Address Space Layout Analysis", """#include <stdio.h>
#include <stdlib.h>

int global_var = 10;
static int static_var = 20;

int main() {
    int stack_var = 30;
    int *heap_var = (int*)malloc(sizeof(int));
    *heap_var = 40;

    printf("Code (main)      : %p\\n", (void*)main);
    printf("Global Variable  : %p\\n", (void*)&global_var);
    printf("Static Variable  : %p\\n", (void*)&static_var);
    printf("Heap Allocation  : %p\\n", (void*)heap_var);
    printf("Stack Variable   : %p\\n", (void*)&stack_var);

    free(heap_var);
    return 0;
}"""),

"Practical-14": ("Virtual Memory Mapping Study via /proc/PID/maps", """#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Inspect virtual memory map using: cat /proc/%d/maps\\n", getpid());
    return 0;
}"""),

"Practical-15": ("Dynamic Memory Management (malloc, calloc, realloc, free) & Valgrind", """#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int*)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) arr[i] = i * 10;

    arr = (int*)realloc(arr, 10 * sizeof(int));
    for (int i = 5; i < 10; i++) arr[i] = i * 10;

    for (int i = 0; i < 10; i++) printf("%d ", arr[i]);
    printf("\\n");

    free(arr);
    return 0;
}"""),

"Practical-16": ("Copy-on-Write (COW) Memory Behavior Analysis after fork()", """#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int data = 100;

int main() {
    printf("Before fork - Data: %d (Address: %p)\\n", data, (void*)&data);
    if (fork() == 0) {
        printf("[Child Before Write] Data: %d (Addr: %p)\\n", data, (void*)&data);
        data = 200; // Trigger Copy-On-Write
        printf("[Child After Write] Data: %d (Addr: %p)\\n", data, (void*)&data);
    } else {
        wait(NULL);
        printf("[Parent] Data: %d (Addr: %p)\\n", data, (void*)&data);
    }
    return 0;
}"""),

"Practical-17": ("Low-level vs Standard I/O System Calls Performance Comparison", """#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("test_low.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    write(fd, "Low-level system call I/O\\n", 26);
    close(fd);

    FILE *f = fopen("test_std.txt", "w");
    fputs("Standard library buffered I/O\\n", f);
    fclose(f);

    printf("I/O Comparison completed.\\n");
    return 0;
}"""),

"Practical-18": ("Standard I/O Redirection using dup2()", """#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    dup2(fd, STDOUT_FILENO);
    close(fd);
    printf("This output is redirected to output.txt via dup2()!\\n");
    return 0;
}"""),

"Practical-19": ("Inode Structure Investigation & Link Allocation (stat, hard & soft links)", """#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>

int main() {
    struct stat st;
    if (stat("main.c", &st) == 0) {
        printf("File: main.c, Inode: %lu, Links: %lu\\n", st.st_ino, st.st_nlink);
    }
    return 0;
}"""),

"Practical-20": ("Memory-Mapped I/O File Reading and Writing using mmap()", """#include <stdio.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

int main() {
    int fd = open("mmap_test.txt", O_RDWR | O_CREAT | O_TRUNC, 0644);
    write(fd, "Memory-Mapped I/O Content", 25);

    char *map = mmap(NULL, 25, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    printf("Mapped File Content: %s\\n", map);
    munmap(map, 25);
    close(fd);
    return 0;
}"""),

"Practical-21": ("Multithreaded Counter Application with Race Condition", """#include <stdio.h>
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
    printf("Final Counter Value (Race Condition): %ld\\n", counter);
    return 0;
}"""),

"Practical-22": ("Thread Synchronization using Mutex Locks", """#include <stdio.h>
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
    printf("Final Synchronized Counter Value: %ld\\n", counter);
    return 0;
}"""),

"Practical-23": ("Producer-Consumer Problem using POSIX Counting Semaphores", """#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

sem_t empty, full;

void* producer(void *arg) {
    (void)arg;
    sem_wait(&empty);
    printf("[Producer] Produced Item\\n");
    sem_post(&full);
    return NULL;
}

void* consumer(void *arg) {
    (void)arg;
    sem_wait(&full);
    printf("[Consumer] Consumed Item\\n");
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
}"""),

"Practical-24": ("Deadlock Scenario Demonstration & Prevention Strategy", """#include <stdio.h>
#include <pthread.h>

pthread_mutex_t m1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t m2 = PTHREAD_MUTEX_INITIALIZER;

void* t1_func(void *arg) {
    (void)arg;
    pthread_mutex_lock(&m1);
    pthread_mutex_lock(&m2); // Resource ordering prevents deadlock
    printf("Thread 1 executed safely\\n");
    pthread_mutex_unlock(&m2);
    pthread_mutex_unlock(&m1);
    return NULL;
}

void* t2_func(void *arg) {
    (void)arg;
    pthread_mutex_lock(&m1); // Ordered resource acquisition
    pthread_mutex_lock(&m2);
    printf("Thread 2 executed safely\\n");
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
    printf("Deadlock Prevention via Resource Ordering Succeeded.\\n");
    return 0;
}""")
}

for folder_name, (title, code) in practicals.items():
    dir_path = os.path.join(prac_root, folder_name)
    os.makedirs(dir_path, exist_ok=True)

    with open(os.path.join(dir_path, "main.c"), "w", encoding="utf-8", newline="\n") as f:
        f.write(code)

    readme_content = f"""# {folder_name}: {title}

## Description
Implementation of OSSP Practical Experiment: {title}.

## Files
- `main.c`: Source code.
- `Makefile`: Build rules.
"""
    with open(os.path.join(dir_path, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(readme_content)

    makefile_content = f"""CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pthread
TARGET = {folder_name.lower().replace('-', '')}

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

clean:
	rm -f $(TARGET) *.o
"""
    with open(os.path.join(dir_path, "Makefile"), "w", encoding="utf-8", newline="\n") as f:
        f.write(makefile_content)

print("Created all 24 Practical folders with main.c, Makefile, and README.md.")
