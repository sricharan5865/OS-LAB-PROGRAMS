#include <stdio.h>
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
}